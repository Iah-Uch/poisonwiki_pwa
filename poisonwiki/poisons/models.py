from django.db import models
from django_currentuser.db.models import CurrentUserField
from core.validators import validate_img
from ckeditor.fields import RichTextField
from django.utils.html import format_html

# Create your models here.
class Poison(models.Model):
    class ContaminationType(models.TextChoices):
        INJECTABLE = "INJ", "Injectable"
        INGESTIBLE = "ING", "Ingestible"
        INHALABLE = "INH", "Inhalable"
        CONTACT = "CON", "Contact"
        OTHER = "OTH", "Other"
        
    name = models.CharField(max_length=40, verbose_name="Name")
    scientific_name = models.CharField(max_length=40, verbose_name="Scientific Name")
    
    contamination_type = models.CharField(
        max_length=3,
        choices=ContaminationType.choices,
        default=ContaminationType.OTHER,
        verbose_name="Contamination Type",
    )
    description = RichTextField(verbose_name="Description", default="<h3>Sem Informações Adicionais</h3>")
    symptoms = RichTextField(verbose_name="Symptoms", default="<h3>Sem Informações Adicionais</h3>")
    treatment = RichTextField(verbose_name="Treatment", default="<h3>Sem Informações Adicionais</h3>")
    
    
    image = models.ImageField(upload_to="poisons/imgs/", verbose_name="Image", validators=[validate_img])
    info_url = models.URLField(verbose_name="Info URL")
    
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    created_by = CurrentUserField(
        on_delete=models.CASCADE,
        editable=False,
        verbose_name="Author",
    )

    def __str__(self):
        return self.name
    
    @property
    def html_description(self):
        return format_html(self.description)
    
    @property
    def html_symptoms(self):
        return format_html(self.symptoms)
    
    @property
    def html_treatment(self):
        return format_html(self.treatment)
