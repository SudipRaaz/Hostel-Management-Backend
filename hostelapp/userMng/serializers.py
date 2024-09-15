from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ('name','email', 'password', 'gender', 'phone_number', 'address', 'date_of_birth','is_active', 'admissionDate', 'seatID')
        extra_kwargs = {'password': {'write_only': True}, }
    def create(self, validated_user):
        password = validated_user.pop('password', None)
        instance = self.Meta.model(**validated_user)
        if password:
            instance.set_password(password)
        instance.save()
        return instance
