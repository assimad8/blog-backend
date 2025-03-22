from rest_framework import serializers

from core.user.serializer import UserSerializer
from core.user.models import User

class RegisterSerializer(UserSerializer):
    # Registration serializer for requests and user creation
    password = serializers.CharField(max_length=128,min_length=8,write_only=True,required=True)

    class Meta:
        model = User
        fields = [
            "id", 
            "username", 
            "first_name", 
            "last_name", 
            "email",
            "password", 
            "phone_number",
            "profile_picture",
            "date_of_birth", 
            "address", 
            "bio", 
            "website", 
            "gender",
            "preferred_language", 
            "user_type", 
        ]
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

