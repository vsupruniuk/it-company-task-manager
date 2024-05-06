from django import forms
from manager.models import Position


class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ("name",)
