from rest_framework.permissions import BasePermission, SAFE_METHODS

class UserPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check permissions for Post
        if view.basename == 'post':
            if request.method in SAFE_METHODS:
                return True  # Read permissions are allowed for everyone
            
            # Allow only the post author to update or delete the post
            if request.method in ['PUT', 'PATCH', 'DELETE'] and obj.author == request.user:
                return True  # Only the post author can modify or delete the post
        
        # Check permissions for Comment
        elif view.basename == 'post-comment':
            if request.method in SAFE_METHODS:
                return True  # Read permissions are allowed for everyone
            
            # Allow only the comment author to modify or delete the comment
            if request.method in ['PUT', 'PATCH', 'DELETE'] and obj.author == request.user:
                return True  # Only the comment author can modify or delete the comment

        return False  # Deny any other actions
        
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True  # Read permissions are allowed for everyone
        if view.basename in ['post', 'post-comment']:
            return bool(request.user and request.user.is_authenticated)
