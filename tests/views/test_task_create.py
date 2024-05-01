from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from manager.models import Project, Task, TaskType, Tag


class PublicTaskCreateTests(TestCase):
    def setUp(self) -> None:
        self.url = reverse("manager:task-create", kwargs={"pk": 1})

    def test_tag_create_login_required(self) -> None:
        res = self.client.get(self.url)

        self.assertEqual(res.status_code, 302)
        self.assertEqual("/accounts/login/?next=/projects/1/tasks/create/", res.url)


class PrivateTaskCreateTests(TestCase):
    def setUp(self) -> None:
        self.project = Project.objects.create(
            name="YouTube",
            description="Copy of YouTube video hosting",
            start_date=datetime(2024, 1, 1),
            budget=100_000_000,
        )

        self.url = reverse(
            "manager:task-create",
            kwargs={"pk": self.project.pk},
        )

        self.user = get_user_model().objects.create_user(
            first_name="Admin",
            last_name="User",
            username="admin",
            password="Qwerty12345!",
        )

        self.client.force_login(self.user)

        self.task_type = TaskType.objects.create(name="Feature", project=self.project)
        self.tag = Tag.objects.create(name="backend", project=self.project)

    def test_should_be_possible_to_create_task(self) -> None:
        form_data = {
            "name": "Create DB structure",
            "description": "Create DB structure for app",
            "deadline": datetime(2024, 5, 10).strftime("%Y-%m-%d"),
            "priority": "high",
            "task_type": self.task_type.id,
            "reporter": self.user.id,
            "assignees": self.user.id,
            "tags": self.tag.id,
        }

        res = self.client.post(self.url, data=form_data)

        self.assertEqual(res.status_code, 302)

        created_task = Task.objects.get(name=form_data["name"])

        self.assertEqual(created_task.name, form_data["name"])
        self.assertEqual(created_task.description, form_data["description"])
        self.assertEqual(
            created_task.deadline.strftime("%Y-%m-%d"), form_data["deadline"]
        )
        self.assertEqual(created_task.priority, form_data["priority"])
        self.assertEqual(created_task.task_type.id, form_data["task_type"])
        self.assertEqual(created_task.reporter.id, form_data["reporter"])

    def test_should_use_proper_template(self) -> None:
        res = self.client.get(self.url)

        self.assertTemplateUsed(res, "manager/task_form.html")
