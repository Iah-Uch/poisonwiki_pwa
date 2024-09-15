from django import template
from PIL import Image

register = template.Library()


@register.filter(is_safe=True)
def get_format(value):
    ext = Image.open(value).format
    return ext