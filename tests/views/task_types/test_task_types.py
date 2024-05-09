from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from manager.models import Project, TaskType
from manager.services import get_project_task_types


class PublicTaskTypesViewTests(TestCase):
    def setUp(self) -> None:
        self.url = reverse("manager:task-type-list", kwargs={"pk": 1})

    def test_task_types_login_required(self) -> None:
        res = self.client.get(self.url)

        self.assertEqual(res.status_code, 302)
        self.assertEqual(res.url, "/accounts/login/?next=/projects/1/task-types/")


class PrivateTaskTypesViewTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            first_name="Admin",
            last_name="User",
            username="admin",
            password="Qwerty12345!",
        )

        self.client.force_login(self.user)

        self.project = Project.objects.create(
            name="YouTube video hosting",
            start_date=datetime(2024, 1, 1),
            budget=100_000_000,
        )

        self.url = reverse("manager:task-type-list", kwargs={"pk": self.project.pk})

        TaskType.objects.create(name="Feature", project=self.project)
        TaskType.objects.create(name="Bug", project=self.project)
        TaskType.objects.create(name="Maintenance", project=self.project)
        TaskType.objects.create(name="Enhancement", project=self.project)
        TaskType.objects.create(name="Refactor", project=self.project)
        TaskType.objects.create(name="Documentation", project=self.project)
        TaskType.objects.create(name="Testing", project=self.project)
        TaskType.objects.create(name="Deployment", project=self.project)
        TaskType.objects.create(name="Research", project=self.project)
        TaskType.objects.create(name="Meeting", project=self.project)
        TaskType.objects.create(name="Training", project=self.project)

    def test_should_display_list_of_task_types(self) -> None:
        task_types = get_project_task_types(self.project.id)

        res = self.client.get(self.url)

        self.assertEqual(list(res.context["task_type_list"]), list(task_types)[:10])

    def test_should_display_list_of_task_types_with_pagination(self) -> None:
        task_types = get_project_task_types(self.project.id)

        res = self.client.get(self.url + "?page=2")

        self.assertEqual(list(res.context["task_type_list"]), list(task_types)[10:])

    def test_should_display_list_of_task_types_with_search(self) -> None:
        task_types = get_project_task_types(self.project.id, task_type_name="feat")

        res = self.client.get(self.url + "?task-type-name=feat")

        self.assertEqual(list(res.context["task_type_list"]), list(task_types)[:1])

    def test_should_use_proper_template(self) -> None:
        res = self.client.get(self.url)

        self.assertTemplateUsed(res, "manager/task_type_list.html")
