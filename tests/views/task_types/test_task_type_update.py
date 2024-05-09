from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from manager.models import Project, TaskType


class PublicTaskTypeUpdateTests(TestCase):
    def setUp(self) -> None:
        self.url = reverse("manager:task-type-update", kwargs={"pk": 1})

    def test_task_type_update_login_required(self) -> None:
        res = self.client.get(self.url)

        self.assertEqual(res.status_code, 302)
        self.assertEqual("/accounts/login/?next=/task-types/1/update/", res.url)


class PrivateTaskTypeUpdateTests(TestCase):
    def setUp(self) -> None:
        self.project = Project.objects.create(
            name="YouTube",
            description="Copy of YouTube video hosting",
            start_date=datetime(2024, 1, 1),
            budget=100_000_000,
        )

        self.task_type = TaskType.objects.create(name="Feature", project=self.project)

        self.url = reverse(
            "manager:task-type-update",
            kwargs={"pk": self.task_type.pk},
        )

        self.user = get_user_model().objects.create_user(
            first_name="Admin",
            last_name="User",
            username="admin",
            password="Qwerty12345!",
        )

        self.client.force_login(self.user)

    def test_should_be_possible_to_update_task_type(self) -> None:
        name = "Bugfix"
        form_data = {"name": name}

        self.client.post(self.url, data=form_data)

        updated_task_type = TaskType.objects.get(name=name)

        self.assertEqual(updated_task_type.name, name)

    def test_should_use_proper_template(self) -> None:
        res = self.client.get(self.url)

        self.assertTemplateUsed(res, "manager/task_type_form.html")
