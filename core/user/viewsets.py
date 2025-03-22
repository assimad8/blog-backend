from rest_framework.permissions import IsAuthenticated
from core.abstract.viewsets import AbstractViewSet
from core.user.serializer import UserSerializer
from django.contrib.auth import get_user_model

user = get_user_model()

class UserViewSet(AbstractViewSet):
    http_method_names = ('get','patch')
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    
    def get_queryset(self):
        if self.request.user.is_superuser:
            return user.objects.all()
        return user.objects.exclude(is_superuser=True)
    
    def get_object(self):
        obj = user.objects.get_object_by_id(self.kwargs["pk"])
        self.check_object_permissions(self.request,obj)
        return obj