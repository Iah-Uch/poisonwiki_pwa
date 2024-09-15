from django.core.exceptions import ValidationError
from django.utils import timezone
from PIL import Image

def validate_img(value):
    ext = Image.open(value).format

    if ext == "JPEG" or ext == "PNG":
        if value.size < 10485760:  # 10mb Image size limit
            return True
        else:
            raise ValidationError("The maximum file size that can be uploaded is 10MB")
    else:
        raise ValidationError("Format Not Allowed!")


def future_date(date):
    if date > timezone.now():
        raise ValidationError("Datas não podem estar no futuro!")


def min_file_size(value, threshold: int = 1):
    if value.size < threshold * 1024:
        raise ValidationError(f"File size must be at least {threshold}KB")


def max_file_size(value, threshold: int = 8):
    if value.size > threshold * 1024 * 1024:
        raise ValidationError(f"File size must not exceed {threshold}MB")
