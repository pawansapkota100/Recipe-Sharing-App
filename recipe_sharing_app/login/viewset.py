from rest_framework import generics,permissions
from rest_framework.viewsets import ViewSet
from .serializer import RegistrationSerializer,ProfileSerializer,LoginSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from .models import Profile
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from core.models import Recipe



class RegisterViewset(generics.CreateAPIView):
    serializer_class= RegistrationSerializer

class LoginViewSet(ViewSet):
    def create(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            if user:
                login(request, user)  # Log the user in
                return Response({'detail': 'Login successful'})
        return Response({'detail': 'Invalid credentials'})

class ProfileUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.profile

    def perform_update(self, serializer):
        serializer.save()
   
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Profile
from login.serializer import ProfileSerializer
from core.serializer import RecipeSerializer
from core.models import Feed
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def follow_user(self, request, pk=None):
        followed_profile = self.get_object()
        user_profile = request.user.profile

        if user_profile != followed_profile:  # Ensure users cannot follow themselves
            user_profile.following.add(followed_profile.user)
            return Response({'message': 'Successfully followed'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Cannot follow yourself'}, status=status.HTTP_400_BAD_REQUEST)

    def unfollow_user(self, request, pk=None):
        unfollowed_profile = self.get_object()
        user_profile = request.user.profile
        user_profile.following.remove(unfollowed_profile.user)
        return Response({'message': 'Successfully unfollowed'}, status=status.HTTP_200_OK)

    def get_feed(self, request):
        user_profile = request.user.profile
        following_profiles = user_profile.following.all()
        following_users = [profile.user for profile in following_profiles]
        feed = Feed.objects.filter(user__in=following_users).order_by('-timestamp')
        serializer = RecipeSerializer(feed, many=True)
        return Response(serializer.data)

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticated]
