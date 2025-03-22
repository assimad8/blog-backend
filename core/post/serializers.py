from rest_framework import serializers

from core.abstract.serializers import AbstractSerializer
from core.user.models import User
from core.user.serializer import UserSerializer,AuthorSerializer
from core.post.models import Post

class PostSerializer(AbstractSerializer):
    author = serializers.SlugRelatedField(queryset=User.objects.all(),slug_field='public_id')

    class Meta:
        model = Post
        fields = [
            'id', 
            'author', 
            'title', 
            'content', 
            'image', 
            'video', 
            'file', 
            'category', 
            'tags',  
            'is_edited', 
            'likes_count', 
            'views_count',
            'is_published', 
            'published_at', 
            'created', 
            'updated'
        ]
        read_only_fields = ['likes', 'views', 'created', 'updated','is_edited']

    def validate_author(self, value):
        if self.context["request"].user != value:
            raise serializers.ValidationError("You can't create a post for another user.")
        return value
    def to_representation(self, instance):
        rep = super().to_representation(instance)

        author = User.objects.get_object_by_id(rep["author"])
        rep['author'] = AuthorSerializer(author).data
        return rep

    def update(self, instance, validated_data):
        if not instance.is_edited:
            validated_data['is_edited'] = True
        instance = super().updated(instance,validated_data)
        return instance
