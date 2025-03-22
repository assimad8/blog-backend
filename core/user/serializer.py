from rest_framework import serializers
from core.abstract.serializers import AbstractSerializer
from core.user.models import User

class UserSerializer(AbstractSerializer):
    password = serializers.CharField(write_only=True, required=False)  # Hide password
    class Meta:
        model = User
        fields = [
            "id", "username", "first_name", "last_name", "email","password", "phone_number",
            "profile_picture", "date_of_birth", "address", "bio", "website", "gender",
            "is_verified", "preferred_language", "user_type", "is_active", "created", "updated"
        ]
        read_only_fields = ["is_verified"]  # Read-only fields

class AuthorSerializer(AbstractSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'gender', 'user_type']