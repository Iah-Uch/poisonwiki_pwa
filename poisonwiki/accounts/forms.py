# forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout, ButtonHolder, Submit, Button
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from authtools.forms import UserCreationForm
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.models import Group

User = get_user_model()


class GroupAdminForm(forms.ModelForm):
    """
    Admin form for creating and updating Group instances with users.

    Attributes:
        users (ModelMultipleChoiceField): Multiple choice field for selecting users.

    Meta:
        model (Group): The Group model.
        exclude (list): List of fields to exclude from the form.

    Methods:
        __init__(): Initializes the form and handles users field initialization and saving.
        save_m2m(): Saves the many-to-many data for the users field.
        save(): Overrides the default save method to save many-to-many data.
    """

    class Meta:
        model = Group
        exclude = []

    users = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        required=False,
        widget=FilteredSelectMultiple("users", False),
    )

    def __init__(self, *args, **kwargs):
        super(GroupAdminForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields["users"].initial = self.instance.user_set.all()

    def save_m2m(self):
        self.instance.user_set.set(self.cleaned_data["users"])

    def save(self, *args, **kwargs):
        instance = super(GroupAdminForm, self).save()
        self.save_m2m()
        return instance


class SignUpForm(UserCreationForm):
    """
    A UserCreationForm with optional password inputs.
    """

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = "POST"
        self.helper.form_tag = True
        self.error_text_inline = True
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Field(
                "name",
                css_class="form-control-lg",
                placeholder="Nome",
            ),
            Field(
                "email",
                css_class="form-control-lg",
                placeholder="Email",
                type="email",
            ),
            Field("password1", css_class="form-control-lg", placeholder="Senha"),
            Field(
                "password2",
                css_class="form-control-lg",
                placeholder="Confirme sua Senha",
            ),
            ButtonHolder(
                Submit("submit", "Criar", css_class="w-75 form-control-lg"),
                css_class="mb-3 text-center",
            ),
        )

        self.fields["password1"].required = False
        self.fields["password2"].required = False
        self.fields["password1"].widget.attrs.update({"autocomplete": "new-password"})
        self.fields["password2"].widget.attrs.update({"autocomplete": "new-password"})


class CrispyLoginForm(AuthenticationForm):
    """
    Custom login form using Crispy Forms.

    Attributes:
        username (CharField): CharField for entering the username (email).

    Meta:
        model (User): The User model.

    Methods:
        __init__(): Initializes the form and sets up the Crispy Forms layout.
    """

    username = forms.CharField(
        max_length=254,
        label="Email",
        widget=forms.EmailInput(attrs={"autofocus": True}),
    )

    class Meta:
        model = User

    def __init__(self, *args, **kwargs):
        super(CrispyLoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = "POST"
        self.helper.form_tag = True
        self.error_text_inline = True
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Field(
                "username",
                css_class="form-control-lg",
                placeholder="Email",
                type="email",
            ),
            Field("password", css_class="form-control-lg", placeholder="Senha"),
            ButtonHolder(
                Submit("submit", "Entrar", css_class="w-75 form-control-lg"),
                css_class="mb-3 text-center",
            ),
        )
