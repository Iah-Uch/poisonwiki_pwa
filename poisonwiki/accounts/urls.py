from django.urls import path
from .views import SignUpView, SignInView, CustomLogoutView
from django.contrib.auth import views as auth_views

app_name = "accounts"

urlpatterns = [
    path("signin/", SignInView.as_view(), name="sign_in"),
    path("signup/", SignUpView.as_view(), name="sign_up"),
    path("signout/", CustomLogoutView.as_view(), name="sign_out"),
    path(
        "password_change/",
        auth_views.PasswordChangeView.as_view(),
        name="password_change",
    ),
    path(
        "password_change/done/",
        auth_views.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    path(
        "password_reset/", auth_views.PasswordResetView.as_view(), name="password_reset"
    ),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]
