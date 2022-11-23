from rest_framework import  serializers
from django.contrib.auth import authenticate
from .models import User

class RegisterSerializer(serializers.Serializer):

    '''
    serializer for sign-in
    '''
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.CharField()
    age = serializers.IntegerField()
    phone = serializers.CharField()

    class Meta:

        model = User
        fields = ['email','username','phone','age','password']

    def create(self, validated_data):

        user = User.objects.create_user(
            email=validated_data['email'], 
            username=validated_data['username'], 
            phone=validated_data['phone'], 
            age=validated_data['age'], 
            password=validated_data['password']
            )
        
        user.save()
        
        return user

class SigninSerializer(serializers.Serializer):

    '''
    serializer for login
    '''

    username = serializers.CharField()
    password = serializers.CharField()

    class Meta:

        model = User
        fields = ['username','password']

    def validate(self, data):
        user = authenticate(data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("invalid provided credentials.")