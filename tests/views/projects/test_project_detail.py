from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from manager.models import Project


class PublicProjectDetailTests(TestCase):
    def setUp(self) -> None:
        self.url = reverse("manager:project-detail", kwargs={"pk": 1})

    def test_project_detail_login_required(self) -> None:
        res = self.client.get(self.url)

        self.assertEqual(res.status_code, 302)
        self.assertEqual("/accounts/login/?next=/projects/1/", res.url)


class PrivateProjectDetailTests(TestCase):
    def setUp(self) -> None:
        self.project = Project.objects.create(
            name="YouTube",
            description="Copy of YouTube video hosting",
            start_date=datetime(2024, 1, 1),
            budget=100_000_000,
        )
        self.url = reverse("manager:project-detail", kwargs={"pk": self.project.pk})

        self.user = get_user_model().objects.create_user(
            first_name="Admin",
            last_name="User",
            username="admin",
            password="Qwerty12345!",
        )

        self.client.force_login(self.user)

    def test_should_display_project_details(self) -> None:
        res = self.client.get(self.url)

        self.assertContains(res, self.project.name)
        self.assertContains(res, self.project.description)
        self.assertContains(res, self.project.start_date.strftime("%b. %#d, %Y"))
        self.assertContains(res, "{:,}$".format(self.project.budget))

    def test_should_use_proper_template(self) -> None:
        res = self.client.get(self.url)

        self.assertTemplateUsed(res, "manager/project_detail.html")
