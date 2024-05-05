from django import forms

from manager.models import Team, Project


class TeamForm(forms.ModelForm):
    projects = forms.ModelMultipleChoiceField(
        queryset=Project.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Team
        fields = ("name", "team_lead", "projects")
