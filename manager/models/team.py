from django.db import models

from task_manager.settings import AUTH_USER_MODEL


class Team(models.Model):
    name = models.CharField(max_length=255)

    team_lead = models.ForeignKey(
        to=AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="team_lead",
        null=True,
        blank=True,
    )
    projects = models.ManyToManyField(to="Project", related_name="teams", blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"Team: {self.name}"
