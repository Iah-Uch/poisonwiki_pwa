from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordResetForm
from django.utils.crypto import get_random_string
from authtools.admin import NamedUserAdmin
from django.contrib import admin
from .forms import SignUpForm, GroupAdminForm
from django.contrib.auth.models import Group

User = get_user_model()


# Unregister the original Group admin.
admin.site.unregister(Group)


class GroupAdmin(admin.ModelAdmin):
    form = GroupAdminForm

    filter_horizontal = ["permissions"]


admin.site.register(Group, GroupAdmin)


class UserAdmin(NamedUserAdmin):
    """
    A UserAdmin that sends a password-reset email when creating a new user,
    unless a password was entered.
    """

    search_fields = (
        "name",
        "email",
    )
    ordering = ("name",)

    add_form = SignUpForm
    add_fieldsets = (
        (
            None,
            {
                "description": (
                    "Insira o nome, email e associação do usuário."
                    " O usuário receberá um email com um link para acessar"
                    " o sistema e definir sua senha."
                ),
                "fields": (
                    "name",
                    "email",
                ),
            },
        ),
        (
            "Senha",
            {
                "description": "Opcionalmente, pode-se definir uma senha aqui. Caso não defina, um link de alteração será enviado ao email.",
                "fields": ("password1", "password2"),
                # 'classes': ('collapse', 'collapse-closed'),
            },
        ),
    )

    def save_model(
        self, request, obj, form, change
    ):  # Saves user and sends a password setting email
        if not change and (
            not form.cleaned_data["password1"] or not obj.has_usable_password()
        ):
            # Django's PasswordResetForm won't let us reset an unusable
            # password. We set it above super() so we don't have to save twice.
            obj.set_password(get_random_string(length=8))
            obj.save()
            reset_password = True
        else:
            reset_password = False

        super(UserAdmin, self).save_model(request, obj, form, change)

        if reset_password:
            reset_form = PasswordResetForm({"email": obj.email})
            assert reset_form.is_valid()
            reset_form.save(
                request=request,
                use_https=request.is_secure(),
                # subject_template_name='registration/account_creation_subject.txt',
                email_template_name="registration/account_creation_email.html",
            )


admin.site.register(User, UserAdmin)
