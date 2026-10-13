from django.urls import path
from rest_framework.routers import DefaultRouter

from users.views import UserViewSet, AuthTokenObtainView

router = DefaultRouter()
router.register("users", UserViewSet)

urlpatterns = [
    path("users/token/", AuthTokenObtainView.as_view(), name="token")
]
urlpatterns += router.urls
