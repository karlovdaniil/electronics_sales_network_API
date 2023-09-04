from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.urls import reverse
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework.permissions import AllowAny

from users.models import User
from users.serializers import UserCreateSerializer, ProfileSerializer, LoginSerializer


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]


class ProfileView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer

    def get_object(self):
        return self.request.user


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        login(request=self.request, user=serializer.save())
        return redirect(reverse('link-list'))


class LogoutView(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer

    @staticmethod
    def get(request, *args, **kwargs):
        logout(request)
        return redirect(reverse('login-user'))
