from django.contrib.auth import get_user_model
from rest_framework import viewsets, renderers
from rest_framework.authtoken.views import ObtainAuthToken

from users.serializers import UserSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AuthTokenObtainView(ObtainAuthToken):
    renderer_classes =  (
        renderers.JSONRenderer,
        renderers.BrowsableAPIRenderer,
    )
