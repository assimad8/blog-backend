from rest_framework.permissions import BasePermission, SAFE_METHODS

class UserPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True  # Read permissions are allowed for everyone
        return bool(request.user and request.user.is_authenticated) if getattr(view, 'basename', None) == 'post' else False

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True  # Read permissions are allowed for everyone
        return bool(request.user and request.user.is_authenticated) if getattr(view, 'basename', None) == 'post' else False
