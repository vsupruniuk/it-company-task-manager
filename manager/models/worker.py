from django.contrib.auth.models import AbstractUser
from django.db import models


class Worker(AbstractUser):
    position = models.ForeignKey(to="Position", on_delete=models.SET_NULL, null=True)
    team = models.ForeignKey(
        to="Team", on_delete=models.SET_NULL, null=True, related_name="workers"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "worker"
        verbose_name_plural = "workers"

    def __str__(self) -> str:
        return f"Worker: {self.username} ({self.first_name} {self.last_name}), {self.position.name}"
