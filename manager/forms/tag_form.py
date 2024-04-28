from django import forms

from manager.models import Tag


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ("name",)
