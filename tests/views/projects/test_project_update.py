from datetime import date

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from manager.models import Project


class PublicProjectUpdateTests(TestCase):
    def setUp(self) -> None:
        self.url = reverse("manager:project-update", kwargs={"pk": 1})

    def test_project_update_login_required(self) -> None:
        res = self.client.get(self.url)

        self.assertEqual(res.status_code, 302)
        self.assertEqual("/accounts/login/?next=/projects/1/update/", res.url)


class PrivateProjectUpdateTests(TestCase):
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

        self.url = reverse("manager:project-update", kwargs={"pk": project.pk})

    def test_should_update_project(self) -> None:
        form_data = {
            "name": "Twitch",
            "description": "Live streaming platform",
            "start_date": date.today(),
            "budget": 150_000_000,
        }

        self.client.post(self.url, data=form_data)

        updated_project = Project.objects.get(name="Twitch")

        self.assertEqual(updated_project.name, form_data.get("name"))
        self.assertEqual(updated_project.description, form_data.get("description"))
        self.assertEqual(updated_project.start_date, form_data.get("start_date"))
        self.assertEqual(updated_project.budget, form_data.get("budget"))

    def test_should_use_proper_template(self) -> None:
        res = self.client.get(self.url)

        self.assertTemplateUsed(res, "manager/project_form.html")
