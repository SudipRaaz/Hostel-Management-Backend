from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status
import jwt, datetime, pytz
from .models import User
from .serializers import UserSerializer

class RegisterViews(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # The line `return Response(serializer.data, status=status.HTTP_201_CREATED)` in the
            # `post` method of the `RegisterViews` class is returning a response to the client after
            # successfully creating a new user.
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
class LoginViews(APIView):
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
            "id": user.id,
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
        
        return response


class UserView(APIView):
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
    def post(self, request):
        response = Response()
        response.delete_cookie("access_token")
        response.data = {
            "message": "Logout successful"
        }
        return response
