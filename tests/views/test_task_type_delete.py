from datetime import date

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from manager.models import Project, TaskType


class PublicTaskTypeDeleteTests(TestCase):
    def setUp(self) -> None:
        self.url = reverse("manager:task-type-delete", kwargs={"pk": 1, "id": 1})

    def test_task_type_delete_login_required(self) -> None:
        res = self.client.get(self.url)

        self.assertEqual(res.status_code, 302)
        self.assertEqual(
            "/accounts/login/?next=/projects/1/task-types/1/delete/", res.url
        )


class PrivateTaskTypeDeleteTests(TestCase):
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
        self.task_type = TaskType.objects.create(name="Feature", project=self.project)

        self.url = reverse(
            "manager:task-type-delete",
            kwargs={"pk": self.project.pk, "id": self.task_type.id},
        )

    def test_should_delete_task_type(self) -> None:
        self.client.post(self.url)

        created_project = Project.objects.filter(name="Feature")

        self.assertEqual(list(created_project), [])

    def test_should_use_proper_template(self) -> None:
        res = self.client.get(self.url)

        self.assertTemplateUsed(res, "manager/task_type_confirm_delete.html")
