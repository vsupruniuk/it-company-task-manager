from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=63)

    team = models.ForeignKey(to="Team", on_delete=models.CASCADE, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]
        index_together = ["name", "team"]
        unique_together = ["name", "team"]

    def __str__(self) -> str:
        return f"Position: {self.name}"
