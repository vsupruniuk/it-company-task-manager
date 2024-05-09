from datetime import datetime

from django.contrib.admin import AdminSite
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from manager.admin import TagAdmin
from manager.admin_filers import ProjectListFilter
from manager.models import Project, Tag


class TagTests(TestCase):
    def setUp(self) -> None:
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin.user", password="Qwerty12345!"
        )

        self.site = AdminSite()

        self.client.force_login(self.admin_user)

        project = Project.objects.create(
            name="YouTube video hosting",
            start_date=datetime(2024, 1, 1),
            budget=100_000_000,
        )
        self.tag = Tag.objects.create(name="backend", project=project)

        self.tag_admin = TagAdmin(Tag, self.site)

    def test_tag_name_listed(self) -> None:
        url = reverse("admin:manager_tag_changelist")

        res = self.client.get(url)

        self.assertContains(res, self.tag.name)

    def test_tag_project_listed(self) -> None:
        url = reverse("admin:manager_tag_changelist")

        res = self.client.get(url)

        self.assertContains(res, self.tag.project)

    def test_search_by_name(self) -> None:
        self.assertIn("name", self.tag_admin.search_fields)

    def test_filtering_by_project(self) -> None:
        self.assertIn(ProjectListFilter, self.tag_admin.list_filter)
