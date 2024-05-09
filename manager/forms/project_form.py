from datetime import datetime, date

from django import forms
from django.core.exceptions import ValidationError

from manager.models import Project


class ProjectFrom(forms.ModelForm):
    start_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))

    class Meta:
        model = Project
        fields = "__all__"

    def clean_start_date(self) -> datetime:
        project_start_date = self.cleaned_data["start_date"]

        if project_start_date < date.today():
            raise ValidationError("Please, select date in future")

        return project_start_date
