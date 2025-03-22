from rest_framework import serializers
from django.http import Http404
from rest_framework.exceptions import NotFound
from core.abstract.serializers import AbstractSerializer
from core.user.serializer import AuthorSerializer
from core.comment.models import Comment

class CommentSerializer(AbstractSerializer):
    author = serializers.SerializerMethodField()  # Custom method for author
    post = serializers.SerializerMethodField()  # Custom method for post

    def validate_post(self, value):
        if self.instance:
            return self.instance.post
        return value

    def get_author(self, obj):
        try:
            author = obj.author  # Get the author of the comment
            return AuthorSerializer(author).data  # Return full author details
        except AttributeError:
            raise NotFound(detail="Comment not found.")  # Return a more readable error if author is not found

    def get_post(self, obj):
        try:
            post = obj.post.public_id  # Get the post of the comment
            return post 
        except AttributeError:
            raise NotFound(detail="Comment not found.")
        
    def update(self, instance, validated_data):
        if instance is Http404 or None:
            raise NotFound(detail="Comment not found.")
        if not instance.edited:
            validated_data['edited'] = True
        instance = super().update(instance, validated_data)
        return instance
    
    class Meta:
        model = Comment
        fields = ['id', 'author', 'post', 'body', 'edited', 'created', 'updated']
        read_only_fields = ['id', 'author', 'post', 'created', 'updated']
