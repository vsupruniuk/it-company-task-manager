from datetime import date

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from manager.models import Project


class PublicProjectDeleteTests(TestCase):
    def setUp(self) -> None:
        self.url = reverse("manager:project-delete", kwargs={"pk": 1})

    def test_project_delete_login_required(self) -> None:
        res = self.client.get(self.url)

        self.assertEqual(res.status_code, 302)
        self.assertEqual("/accounts/login/?next=/projects/1/delete/", res.url)


class PrivateProjectDeleteTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            first_name="Admin",
            last_name="User",
            username="admin",
            password="Qwerty12345!",
        )

        self.client.force_login(self.user)

        project = Project.objects.create(
            name="YouTube",
            description="YouTube video hosting",
            start_date=date(2024, 1, 1),
            budget=100_000_000,
        )

        self.url = reverse("manager:project-delete", kwargs={"pk": project.pk})

    def test_should_delete_project(self) -> None:
        self.client.post(self.url)

        project = Project.objects.filter(name="YouTube")

        self.assertEqual(list(project), [])

    def test_should_use_proper_template(self) -> None:
        res = self.client.get(self.url)

        self.assertTemplateUsed(res, "manager/project_confirm_delete.html")
