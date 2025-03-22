# from django.http.response import Http404
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from core.abstract.viewsets import AbstractViewSet
from core.comment.models import Comment
from core.comment.serializers import CommentSerializer
from rest_framework.permissions import IsAuthenticated
from core.auth.pemissions import UserPermission
from core.post.models import Post

# Create your views here.

class CommentViewSet(AbstractViewSet):
    http_method_names = ['post','get','put','delete']
    permission_classes = [UserPermission]
    serializer_class = CommentSerializer 
    
    def get_object(self):
        obj = Comment.objects.get_object_by_id(self.kwargs['pk'])
        self.check_object_permissions(self.request,obj)
        return obj
    
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Comment.objects.all()
        post_id = self.kwargs.get('post_pk')  # Get post ID from URL
        return Comment.objects.filter(post__public_id=post_id)  # Only return comments for the specific post
    
    def create(self, request, *args, **kwargs):
        """Customizing comment creation by setting author from JWT and post from URL"""
        post = Post.objects.get(public_id=self.kwargs['post_pk'])  # Get the post from URL
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Save with the authenticated user as author
        serializer.save(author=request.user, post=post)

        return Response({
            "message": "Comment added successfully!",
            "comment": serializer.data
        }, status=status.HTTP_201_CREATED)