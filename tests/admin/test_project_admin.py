from datetime import datetime

from django.contrib.admin import AdminSite
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from manager.admin import ProjectAdmin
from manager.models import Project


class ProjectTests(TestCase):
    def setUp(self) -> None:
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin.user", password="Qwerty12345!"
        )

        self.site = AdminSite()

        self.client.force_login(self.admin_user)

        self.project = Project.objects.create(
            name="YouTube video hosting",
            start_date=datetime(2024, 1, 1),
            budget=100_000_000,
        )

        self.project_admin = ProjectAdmin(Project, self.site)

    def test_project_name_listed(self) -> None:
        url = reverse("admin:manager_project_changelist")

        res = self.client.get(url)

        self.assertContains(res, self.project.name)

    def test_project_start_date_listed(self) -> None:
        url = reverse("admin:manager_project_changelist")

        res = self.client.get(url)

        self.assertContains(res, self.project.start_date.strftime("%b.%e, %Y"))

    def test_project_budget_listed(self) -> None:
        url = reverse("admin:manager_project_changelist")

        res = self.client.get(url)

        self.assertContains(res, self.project.budget)

    def test_search_by_name(self) -> None:
        self.assertIn("name", self.project_admin.search_fields)

    def test_filtering_by_start_date(self) -> None:
        self.assertIn("start_date", self.project_admin.list_filter)
