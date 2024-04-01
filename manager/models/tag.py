from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=63)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]
        # TODO name + project
        index_together = []
        unique_together = []

    def __str__(self) -> str:
        return f"Task type: {self.name}"
