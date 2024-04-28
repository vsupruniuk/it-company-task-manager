from django import forms

from manager.models import TaskType


class TaskTypeForm(forms.ModelForm):
    class Meta:
        model = TaskType
        fields = ("name",)
