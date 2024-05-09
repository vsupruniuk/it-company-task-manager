from datetime import datetime

from django.contrib.admin import AdminSite
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from manager.admin import TaskAdmin
from manager.admin_filers import ProjectListFilter
from manager.models import Task, Position, Project, Team


class TaskTests(TestCase):
    def setUp(self) -> None:
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin.user", password="Qwerty12345!"
        )

        self.site = AdminSite()

        self.client.force_login(self.admin_user)

        team = Team.objects.create(name="Avengers-developers")
        position = Position.objects.create(name="Developer", team=team)
        reporter = get_user_model().objects.create(
            username="t.stark", first_name="Tony", last_name="Stark", position=position
        )
        project = Project.objects.create(
            name="YouTube video hosting",
            start_date=datetime(2024, 1, 1),
            budget=100_000_000,
        )

        self.task = Task.objects.create(
            name="Create DB structure",
            deadline=datetime(2024, 4, 10),
            priority="High",
            reporter=reporter,
            project=project,
        )

        self.task_admin = TaskAdmin(Task, self.site)

    def test_task_name_listed(self) -> None:
        url = reverse("admin:manager_task_changelist")

        res = self.client.get(url)

        self.assertContains(res, self.task.name)

    def test_task_deadline_listed(self) -> None:
        url = reverse("admin:manager_task_changelist")

        res = self.client.get(url)

        self.assertContains(res, self.task.deadline.strftime("%B %d, %Y"))

    def test_task_is_completed_listed(self) -> None:
        url = reverse("admin:manager_task_changelist")

        res = self.client.get(url)

        self.assertContains(res, self.task.is_completed)

    def test_task_priority_listed(self) -> None:
        url = reverse("admin:manager_task_changelist")

        res = self.client.get(url)

        self.assertContains(res, self.task.priority)

    def test_task_reporter_listed(self) -> None:
        url = reverse("admin:manager_task_changelist")

        res = self.client.get(url)

        self.assertContains(res, self.task.reporter)

    def test_task_project_listed(self) -> None:
        url = reverse("admin:manager_task_changelist")

        res = self.client.get(url)

        self.assertContains(res, self.task.project)

    def test_filtering_by_deadline(self) -> None:
        self.assertIn("deadline", self.task_admin.list_filter)

    def test_filtering_by_is_completed(self) -> None:
        self.assertIn("is_completed", self.task_admin.list_filter)

    def test_filtering_by_priority(self) -> None:
        self.assertIn("priority", self.task_admin.list_filter)

    def test_filtering_by_task_type(self) -> None:
        self.assertIn("task_type", self.task_admin.list_filter)

    def test_filtering_by_reporter(self) -> None:
        self.assertIn("reporter", self.task_admin.list_filter)

    def test_filtering_by_project(self) -> None:
        self.assertIn(ProjectListFilter, self.task_admin.list_filter)

    def test_filtering_by_assignees(self) -> None:
        self.assertIn("assignees", self.task_admin.list_filter)

    def test_filtering_by_tags(self) -> None:
        self.assertIn("tags", self.task_admin.list_filter)

    def test_search_by_name(self) -> None:
        self.assertIn("name", self.task_admin.search_fields)
