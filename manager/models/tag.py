from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=63)

    project = models.ForeignKey(to="Project", on_delete=models.CASCADE, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]
        index_together = ["name", "project"]
        unique_together = ["name", "project"]

    def __str__(self) -> str:
        return f"Tag: {self.name}"
