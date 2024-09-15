from django.db import models
from django.utils.translation import gettext_lazy as _
from authtools.models import AbstractNamedUser


class User(AbstractNamedUser):
    """
    Custom user model representing a user associated with an association.

    Attributes:
        association (ForeignKey): Association to which the user belongs.

    Meta:
        verbose_name (str): Singular name for the model.
        verbose_name_plural (str): Plural name for the model.

    USERNAME_FIELD (str): The field used as the unique identifier for authentication (email in this case).
    REQUIRED_FIELDS (tuple): Fields required for creating a user instance.

    Methods:
        __str__(): Returns a human-readable representation of the user.
    """

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("name",)

    class Meta(AbstractNamedUser.Meta):
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return self.name
