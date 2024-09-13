from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status, generics
import jwt, datetime, pytz

from seatMng.views import SeatMngCreateAPIView
from seatMng.serializers import SeatSerializer
from .models import User
from .serializers import UserSerializer


class RegisterViews(APIView):
    # register users and create seat
    def post(self, request, *args, **kwargs):
        # Extract the data from the request
        seat_data = request.data.get('seat')
        user_data = request.data.get('user')
        user_serializer = UserSerializer(data=user_data)

        # Validate and create the seat record first
        seat_creation = SeatMngCreateAPIView()
        seat_response = seat_creation.post(request)
        if seat_response.status_code != status.HTTP_201_CREATED or not user_serializer.is_valid():
            return Response({"error": seat_response.data}, status=seat_response.status_code)
        else:
            # Add the seatID to the user data
            user_data['seatID'] = seat_response.data['seatID'] # type: ignore

            # Create the user record
            if user_serializer.is_valid():
                user_serializer.save()
                return Response({
                    'seat': seat_response.data,
                    'user': user_serializer.data
                }, status=status.HTTP_201_CREATED)
            else:
                # If user data is invalid, return an error
                return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    # get user details from kwargs email path
    def get(self, request, *args, **kwargs):
        email = kwargs.get('email', None)
        if email is None:
            return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        # Serialize the user data
        user_data = UserSerializer(user).data
        
        # Serialize the related seat data
        seat_data = SeatSerializer(user.seatID).data
        
        # Combine the user and seat data into a single response
        combined_data = {
            'user': user_data,
            'seat': seat_data
        }
        
        return Response(combined_data, status=status.HTTP_200_OK)
    
    def put(self, request, *args, **kwargs):
        email = kwargs.get('email', None)
        if email is None:
            return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Retrieve the user and related seat object
        user = get_object_or_404(User.objects.select_related('seatID'), email=email)
        seat = user.seatID
        
        # Separate user and seat data from the request
        user_data = request.data.get('user', {})
        seat_data = request.data.get('seat', {})
        
        # Serialize the user data
        user_serializer = UserSerializer(user, data=user_data, partial=True)
        if user_serializer.is_valid():
            user_serializer.save()
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # Serialize the seat data
        seat_serializer = SeatSerializer(seat, data=seat_data, partial=True)
        if seat_serializer.is_valid():
            seat_serializer.save()
        else:
            return Response(seat_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # Combine updated user and seat data
        combined_data = {
            'user': user_serializer.data,
            'seat': seat_serializer.data
        }
        
        return Response(combined_data, status=status.HTTP_200_OK)
    
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginViews(APIView):
    # login using respective user credentials
    def post(self, request, *args, **kwargs):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if not user:
            raise AuthenticationFailed('User not found')
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')
        
        # Get the current time in UTC and then convert it to Nepal time
        nepal_timezone = pytz.timezone('Asia/Kathmandu')
        current_time_nepal = datetime.datetime.now(nepal_timezone)
        expiry_time_nepal = current_time_nepal + datetime.timedelta(minutes=60)
        
        payload = {
            "id": user.id, # type: ignore
            "email": user.email,
            "exp": expiry_time_nepal.timestamp(),
            "iat": current_time_nepal.timestamp()
        }

        token = jwt.encode(payload, 'secret_key', algorithm='HS256')
        response = Response()
        response.set_cookie(key='access_token', value=token, expires=expiry_time_nepal, httponly=True)
        response.data = {
            "access_token": token,
            "message": "Login successful"
        }
        
        return {response, status.HTTP_200_OK}
    
    # get users details using cookies token
    def get(self, request):
        token = request.COOKIES.get("access_token")
        if not token:
            raise AuthenticationFailed("Token not found")
        try:
            payload = jwt.decode(token, "secret_key", algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Token expired")

        user = User.objects.get(id=payload['id'])

        if not user:
            raise AuthenticationFailed("User not found")

        serializer = UserSerializer(user)
        return Response(serializer.data)


class UserView(APIView):
    """#+
    Retrieve user information using JWT token.#+

        user = User.objects.get(id=payload['id'])#-
    This function retrieves the JWT token from the request cookies, decodes it,#+
    and fetches the user information from the database. If the token is not found,#+
    expired, or the user does not exist, it raises an appropriate authentication error.#+

        if not user:#-
            raise AuthenticationFailed("User not found")#-
    Parameters:#+
    request (Request): The incoming request object containing the JWT token in cookies.#+

        serializer = UserSerializer(user)#-
        return Response(serializer.data)#-
    Returns:#+
    Response: A response object containing the serialized user data if successful.#+
    """#+
    def get(self, request):
        token = request.COOKIES.get("access_token")
        if not token:
            raise AuthenticationFailed("Token not found")
        try:
            payload = jwt.decode(token, "secret_key", algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Token expired")

        user = User.objects.get(id=payload['id'])

        if not user:
            raise AuthenticationFailed("User not found")

        serializer = UserSerializer(user)
        return Response(serializer.data)


class logout(APIView):
    # user log out
    def post(self, request):
        response = Response()
        response.delete_cookie("access_token")
        response.data = {
            "message": "Logout successful"
        }
        return response
