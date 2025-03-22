from rest_framework import serializers

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
        return AuthorSerializer(obj.author).data  # Return full author details

    def get_post(self, obj):
        return obj.post.public_id  # Return post ID as a reference

    def update(self, instance, validated_data):
        if not instance.edited:
            validated_data['edited'] = True
        instance = super().update(instance, validated_data)
        return instance
    
    class Meta:
        model = Comment
        fields = ['id', 'author', 'post', 'body', 'edited', 'created', 'updated']
        read_only_fields = ['id', 'author', 'post', 'created', 'updated']
