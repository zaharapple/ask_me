from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, RedirectView, UpdateView

from user.forms import UserSignUpForm, SignInForm
from user.models import UserProfile


class UserSignUpView(CreateView):
    """User sign-up view implementation"""
    model = User
    form_class = UserSignUpForm
    template_name = "sign-up.html"
    success_url = reverse_lazy("user:sign-in")


class UserSignInView(LoginView):
    """User sign-in view implementation"""
    form_class = SignInForm
    template_name = 'sign-in.html'

    def get_success_url(self):
        return reverse_lazy('main:home')


class UserLogoutView(RedirectView):
    """User logout view implementation"""

    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy('main:home')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(UserLogoutView, self).get(request, *args, **kwargs)


class UserProfileView(TemplateView):
    """User profile view implementation"""

    template_name = "profile.html"

    def get_context_data(self):
        """Return a context data dictionary"""

        user = self.request.user
        try:
            tasks = user.mytest_set.all()

        except UserProfile.DoesNotExist:
            tasks = None

        return {"user": user, "tasks": tasks}


class ProfileUpdate(UpdateView):

    model = UserProfile
    fields = ["birthday","img", "myself_info"]
    template_name = "profile_update.html"
    success_url = reverse_lazy('user:profile')





