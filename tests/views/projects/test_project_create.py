from datetime import date

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from manager.models import Project


class PublicProjectCreateTests(TestCase):
    def setUp(self) -> None:
        self.url = reverse("manager:project-create")

    def test_project_create_login_required(self) -> None:
        res = self.client.get(self.url)

        self.assertEqual(res.status_code, 302)
        self.assertEqual("/accounts/login/?next=/projects/create/", res.url)


class PrivateProjectCreateTests(TestCase):
    def setUp(self) -> None:
        self.url = reverse("manager:project-create")

        self.user = get_user_model().objects.create_user(
            first_name="Admin",
            last_name="User",
            username="admin",
            password="Qwerty12345!",
        )

        self.client.force_login(self.user)

    def test_should_create_project(self) -> None:
        form_data = {
            "name": "YouTube",
            "description": "YouTube video hosting",
            "start_date": date.today(),
            "budget": 100_000_000,
        }

        self.client.post(self.url, data=form_data)

        created_project = Project.objects.get(name="YouTube")

        self.assertEqual(created_project.name, form_data.get("name"))
        self.assertEqual(created_project.description, form_data.get("description"))
        self.assertEqual(created_project.start_date, form_data.get("start_date"))
        self.assertEqual(created_project.budget, form_data.get("budget"))

    def test_should_use_proper_template(self) -> None:
        res = self.client.get(self.url)

        self.assertTemplateUsed(res, "manager/project_form.html")
