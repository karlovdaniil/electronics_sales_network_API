from django.urls import path

from users import views

urlpatterns = [
    path('signup/', views.UserCreateView.as_view(), name='create_user'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]
