from datetime import datetime

from django.contrib.admin import AdminSite
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from manager.admin import TaskTypeAdmin
from manager.admin_filers import ProjectListFilter
from manager.models import Project, TaskType


class TaskTypeTests(TestCase):
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
        self.task_type = TaskType.objects.create(name="Feature", project=project)

        self.task_type_admin = TaskTypeAdmin(TaskType, self.site)

    def test_task_type_name_listed(self) -> None:
        url = reverse("admin:manager_tasktype_changelist")

        res = self.client.get(url)

        self.assertContains(res, self.task_type.name)

    def test_task_type_project_listed(self) -> None:
        url = reverse("admin:manager_tasktype_changelist")

        res = self.client.get(url)

        self.assertContains(res, self.task_type.project)

    def test_search_by_name(self) -> None:
        self.assertIn("name", self.task_type_admin.search_fields)

    def test_filtering_by_project(self) -> None:
        self.assertIn(ProjectListFilter, self.task_type_admin.list_filter)
