"""
Urls user application
=====================
"""
from django.urls import path, include

from user.views import (UserLogoutView, UserSignInView,
                        UserSignUpView, UserProfileView, ProfileUpdate)

app_name = "user"
urlpatterns = [
    path("sign-up/", UserSignUpView.as_view(), name="sign-up"),
    path("sign-in/", UserSignInView.as_view(), name="sign-in"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("profile/<int:pk>/", UserProfileView.as_view(), name="profile"),
    path('update/<int:pk>/', ProfileUpdate.as_view(), name='profile-update'),



]