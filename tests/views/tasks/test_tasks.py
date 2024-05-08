from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from manager.models import Project, Task
from manager.services import get_project_tasks


class PublicTasksViewTests(TestCase):
    def setUp(self) -> None:
        self.url = reverse("manager:task-list", kwargs={"pk": 1})

    def test_tasks_login_required(self) -> None:
        res = self.client.get(self.url)

        self.assertEqual(res.status_code, 302)
        self.assertEqual(res.url, "/accounts/login/?next=/projects/1/tasks/")


class PrivateTasksViewTests(TestCase):
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

        self.url = reverse("manager:task-list", kwargs={"pk": self.project.pk})

        Task.objects.create(
            name="Create DB structure",
            deadline=datetime(2024, 4, 30),
            priority="Highest",
            project=self.project,
        )
        Task.objects.create(
            name="Design front-end layout",
            deadline=datetime(2024, 5, 15),
            priority="High",
            project=self.project,
        )
        Task.objects.create(
            name="Implement user authentication",
            deadline=datetime(2024, 6, 1),
            priority="High",
            project=self.project,
        )
        Task.objects.create(
            name="Set up database backups",
            deadline=datetime(2024, 5, 20),
            priority="Medium",
            project=self.project,
        )
        Task.objects.create(
            name="Optimize query performance",
            deadline=datetime(2024, 7, 5),
            priority="Medium",
            project=self.project,
        )
        Task.objects.create(
            name="Develop API endpoints",
            deadline=datetime(2024, 5, 30),
            priority="High",
            project=self.project,
        )
        Task.objects.create(
            name="Create mobile-responsive design",
            deadline=datetime(2024, 6, 15),
            priority="Medium",
            project=self.project,
        )
        Task.objects.create(
            name="Conduct usability testing",
            deadline=datetime(2024, 8, 10),
            priority="Low",
            project=self.project,
        )
        Task.objects.create(
            name="Prepare user documentation",
            deadline=datetime(2024, 7, 20),
            priority="Low",
            project=self.project,
        )
        Task.objects.create(
            name="Implement continuous integration",
            deadline=datetime(2024, 6, 25),
            priority="High",
            project=self.project,
        )
        Task.objects.create(
            name="Launch marketing campaign",
            deadline=datetime(2024, 9, 1),
            priority="Medium",
            project=self.project,
        )

    def test_should_display_list_of_tasks(self) -> None:
        tasks = get_project_tasks(self.project.id)

        res = self.client.get(self.url)

        self.assertEqual(list(res.context["task_list"]), list(tasks)[:10])

    def test_should_display_list_of_tasks_with_pagination(self) -> None:
        tasks = get_project_tasks(self.project.id)

        res = self.client.get(self.url + "?page=2")

        self.assertEqual(list(res.context["task_list"]), list(tasks)[10:])

    def test_should_display_list_of_tasks_with_search(self) -> None:
        tasks = get_project_tasks(self.project.id, task_name="structure")

        res = self.client.get(self.url + "?task-name=structure")

        self.assertEqual(list(res.context["task_list"]), list(tasks)[:1])

    def test_should_use_proper_template(self) -> None:
        res = self.client.get(self.url)

        self.assertTemplateUsed(res, "manager/task_list.html")
