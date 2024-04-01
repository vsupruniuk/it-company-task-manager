from django.db import models

from task_manager.settings import AUTH_USER_MODEL

PRIORITIES = (
    ("highest", "Highest"),
    ("high", "High"),
    ("medium", "Medium"),
    ("low", "Low"),
    ("lowest", "Lowest"),
)


class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1000, null=True, blank=True)
    deadline = models.DateField()
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=7, choices=PRIORITIES)

    task_type = models.ForeignKey(to="TaskType", on_delete=models.SET_NULL, null=True)
    reporter = models.ForeignKey(
        to=AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True
    )
    project = models.ForeignKey(to="Project", on_delete=models.CASCADE)

    assignees = models.ManyToManyField(to=AUTH_USER_MODEL, related_name="tasks")
    tags = models.ManyToManyField(to="Tag", related_name="tasks")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return (
            f"Task: {self.name} (priority: {self.priority}, deadline: {self.deadline}). "
            f"Assigned to: {self.assignees}"
        )
