import django_filters as df
from django import forms
from django.db.models import Q
from .models import Poison
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout, Column
from crispy_forms.bootstrap import AppendedText
from django.utils.safestring import mark_safe


class PoisonFilter(df.FilterSet):
    search = df.CharFilter(
        method="search_filter",
        label="Search",
        widget=forms.TextInput(
            attrs={"class": "form-control-lg", "placeholder": "Buscar..."}
        ),
    )
    contamination_type = df.MultipleChoiceFilter(
        choices=Poison.ContaminationType.choices,
        widget=forms.CheckboxSelectMultiple(
            attrs={
                "class": "form-check-input d-none",  # hide default checkboxes
            }
        ),
        label="Poison Type",
    )

    class Meta:
        model = Poison
        fields = ["search", "contamination_type"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form.helper = FormHelper()
        self.form.helper.form_tag = False
        self.form.helper.disable_csrf = True
        self.form.fields["search"].label = False
        self.form.helper.layout = Layout(
            Column(
                AppendedText(
                    "search", mark_safe('<i class="bi bi-search text-primary"></i>')
                ),
            ),
            Column(Field("contamination_type")),
        )

    def search_filter(self, queryset, name, value):
        return queryset.filter(
            Q(name__icontains=value)
            | Q(scientific_name__icontains=value)
            | Q(description__icontains=value)
        )
