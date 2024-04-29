from datetime import date, datetime

from django.test import TestCase

from manager.models import Project, Task
from manager.services import get_project_tasks


class GetProjectTasksTests(TestCase):
    def setUp(self) -> None:
        self.project_youtube = Project.objects.create(
            name="YouTube", start_date=date(2024, 1, 1), budget=100_000_000
        )
        self.project_twitch = Project.objects.create(
            name="Twitch", start_date=date(2024, 1, 1), budget=100_000_000
        )

        Task.objects.create(
            name="Create DB structure",
            deadline=datetime(2024, 4, 30),
            priority="Highest",
            project=self.project_youtube,
        )
        Task.objects.create(
            name="Design front-end layout",
            deadline=datetime(2024, 5, 15),
            priority="High",
            project=self.project_youtube,
        )
        Task.objects.create(
            name="Implement user authentication",
            deadline=datetime(2024, 6, 1),
            priority="High",
            project=self.project_twitch,
        )

    def test_should_return_tasks_only_for_specific_project(self) -> None:
        tasks = get_project_tasks(self.project_youtube.id)

        for task in tasks:
            self.assertEqual(task.project, self.project_youtube)

    def test_should_filter_tasks_by_name_if_name_provided(self) -> None:
        tasks = get_project_tasks(self.project_youtube.id, task_name="structure")

        for task in tasks:
            self.assertIn("structure", task.name.lower())
