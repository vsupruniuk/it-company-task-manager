from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1000, null=True, blank=True)
    start_date = models.DateField()
    budget = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]
        indexes = [models.Index(fields=["name"])]

    def __str__(self) -> str:
        date = self.start_date.strftime("%Y-%m-%d")

        return f"Project: {self.name} (budget: {self.budget}, start date: {date})"
