from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from .forms import SignUpForm, CrispyLoginForm
from django.contrib.auth.views import LogoutView

User = get_user_model()


class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    success_url = reverse_lazy("events:list")
    template_name = "registration/signup.html"

    def get_context_data(self, **kwargs):
        context = super(SignUpView, self).get_context_data(**kwargs)
        if not self.request.htmx:
            context["title"] = "SignUp"
        return context


class SignInView(LoginView):
    model = User
    form_class = CrispyLoginForm
    template_name = "registration/login.html"

    def get_context_data(self, **kwargs):
        context = super(SignInView, self).get_context_data(**kwargs)
        if not self.request.htmx:
            context["title"] = "SignIn"
        return context

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        response["clear-cache"] = "true"
        return response


class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        response["clear-cache"] = "true"
        return response
