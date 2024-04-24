from django.urls import path
from .viewset import RegisterViewset,ProfileUpdateAPIView,LoginViewSet
from rest_framework.routers import DefaultRouter
from django.urls import include
router = DefaultRouter()
router.register(r'', LoginViewSet, basename='login')

urlpatterns = [
  path('register/',RegisterViewset.as_view()),
  path('profile/', ProfileUpdateAPIView.as_view(), name='profile-update'),
  path('', include(router.urls))

]