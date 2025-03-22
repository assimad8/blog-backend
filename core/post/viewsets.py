from datetime import timezone
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from core.abstract.viewsets import AbstractViewSet
from core.post.models import Post
from core.post.serializers import PostSerializer

# Create your views here

class PostViewSet(AbstractViewSet):
    http_method_names = ('post','get','put','delete')
    permission_classes = (IsAuthenticated,)
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all()
    
    def get_object(self):
        obj = Post.objects.get_object_by_id(self.kwargs['pk'])
        obj.increment_views_count()  # Update view count when post is accessed
        self.check_object_permissions(self.request,obj)
        return obj
    def create(self,request,*args,**wkargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # Check if post should be published
        if serializer.is_published and not serializer.published_at:
            serializer.published_at = timezone.now()  # Set published_at when publishing
        self.perform_create(serializer)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        # Check if post is being published
        if request.data.get("is_published") and not instance.published_at:
            instance.published_at = timezone.now()

        self.perform_update(serializer)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def like(self, request, pk=None):
        """Endpoint to like/unlike a post"""
        post = self.get_object()
        user = request.user

        # Like or Un-like the post
        if user.has_liked(post):
            user.remove_like(post)  # Unlike the post
            liked = False
        else:
            user.like(post)  # Like the post
            liked = True

        post.update_likes_count()  # Update the post's like count

        return Response({
            "liked": liked,
            "likes_count": post.likes_count
        }, status=status.HTTP_200_OK)
    
    def list(self, request, *args, **kwargs):
        """
        Override the list method to update the view count for all posts.
        """
        queryset = self.get_queryset()
        
        # Update the view count for all posts
        for post in queryset:
            post.increment_views_count()

        # Proceed with the usual list operation
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "posts": serializer.data
        })