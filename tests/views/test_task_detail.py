from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from manager.models import Project, Task


class PublicTaskDetailTests(TestCase):
    def setUp(self) -> None:
        self.url = reverse("manager:task-detail", kwargs={"pk": 1, "id": 1})

    def test_task_detail_login_required(self) -> None:
        res = self.client.get(self.url)

        self.assertEqual(res.status_code, 302)
        self.assertEqual("/accounts/login/?next=/projects/1/tasks/1/", res.url)


class PrivateTaskDetailTests(TestCase):
    def setUp(self) -> None:
        self.project = Project.objects.create(
            name="YouTube",
            description="Copy of YouTube video hosting",
            start_date=datetime(2024, 1, 1),
            budget=100_000_000,
        )
        self.task = Task.objects.create(
            name="Create DB structure",
            deadline=datetime(2024, 5, 10),
            project=self.project,
        )

        self.url = reverse(
            "manager:task-detail",
            kwargs={"pk": self.project.pk, "id": self.task.id},
        )

        self.user = get_user_model().objects.create_user(
            first_name="Admin",
            last_name="User",
            username="admin",
            password="Qwerty12345!",
        )

        self.client.force_login(self.user)

    def test_should_display_task_details(self) -> None:
        res = self.client.get(self.url)

        self.assertContains(res, self.task.name)
        self.assertContains(res, self.task.deadline.strftime("%b %#d, %Y"))
        self.assertContains(res, self.task.project.name)

    def test_should_use_proper_template(self) -> None:
        res = self.client.get(self.url)

        self.assertTemplateUsed(res, "manager/task_detail.html")
