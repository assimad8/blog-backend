from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth.models import update_last_login
from core.user.serializer import UserSerializer

class LoginSerializer(TokenObtainPairSerializer):  # ✅ Change TokenObtainSerializer -> TokenObtainPairSerializer
    def validate(self, attrs):
        data = super().validate(attrs)  # This now properly authenticates the user and sets self.user
        
        # Get JWT tokens
        refresh = self.get_token(self.user)
        
        # Add user data
        data["user"] = UserSerializer(self.user).data
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        
        # Update last login
        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)
        
        return data
