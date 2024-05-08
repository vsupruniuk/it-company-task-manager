from datetime import date

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from manager.models import Project, Task


class PublicTaskDeleteTests(TestCase):
    def setUp(self) -> None:
        self.url = reverse("manager:task-delete", kwargs={"pk": 1})

    def test_task_delete_login_required(self) -> None:
        res = self.client.get(self.url)

        self.assertEqual(res.status_code, 302)
        self.assertEqual("/accounts/login/?next=/tasks/1/delete/", res.url)


class PrivateTaskDeleteTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            first_name="Admin",
            last_name="User",
            username="admin",
            password="Qwerty12345!",
        )

        self.client.force_login(self.user)

        self.project = Project.objects.create(
            name="YouTube",
            description="YouTube video hosting",
            start_date=date(2024, 1, 1),
            budget=100_000_000,
        )

        self.task = Task.objects.create(
            name="Create DB structure",
            deadline=date(2024, 5, 10),
            priority="high",
            project=self.project,
        )

        self.url = reverse("manager:task-delete", kwargs={"pk": self.task.pk})

    def test_should_delete_task(self) -> None:
        self.client.post(self.url)

        task = Task.objects.filter(name="Create DB structure")

        self.assertEqual(list(task), [])

    def test_should_use_proper_template(self) -> None:
        res = self.client.get(self.url)

        self.assertTemplateUsed(res, "manager/task_confirm_delete.html")
