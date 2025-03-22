from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from core.abstract.serializers import AbstractSerializer
from core.user.serializer import UserSerializer,AuthorSerializer
from core.user.models import User
from core.post.models import Post
from core.comment.models import Comment

class CommentSerializer(AbstractSerializer):
    author = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='public_id'
    )
    post = serializers.SlugRelatedField(
        queryset=Post.objects.all(),
        slug_field='public_id'
    )

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        author = User.objects.get_object_by_id(rep["author"])
        rep["author"] = AuthorSerializer(author).data
        return rep
    class Meta:
        model = Comment

        fields = ['id','post','author','body','edited','created','updated']

        read_only_fields = ['edited']





