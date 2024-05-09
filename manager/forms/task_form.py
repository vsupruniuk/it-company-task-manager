from datetime import datetime, date

from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from manager.models import Task, Tag


class TaskForm(forms.ModelForm):
    deadline = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    assignees = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Task
        fields = (
            "name",
            "description",
            "deadline",
            "priority",
            "task_type",
            "reporter",
            "assignees",
            "tags",
        )

    def clean_deadline(self) -> datetime:
        task_deadline = self.cleaned_data["deadline"]

        if task_deadline < date.today():
            raise ValidationError("Please, select date in future")

        return task_deadline
