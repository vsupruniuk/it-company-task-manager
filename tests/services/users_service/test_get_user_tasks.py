from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase

from manager.models import Task, Project
from manager.services import get_user_tasks


class GetUserTasksTests(TestCase):
    def setUp(self) -> None:
        self.worker_tony = get_user_model().objects.create(
            first_name="Tony",
            last_name="Stark",
            username="t.stark",
            email="tony@avanger.com",
            password="Qwerty12345!",
        )

        self.project = Project.objects.create(
            name="YouTube video hosting",
            start_date=datetime(2024, 1, 1),
            budget=100_000_000,
        )

        self.task_create_db_structure = Task.objects.create(
            name="Create DB structure",
            deadline=datetime(2024, 4, 30),
            priority="High",
            project=self.project,
            is_completed=True,
        )
        self.task_create_design = Task.objects.create(
            name="Create design",
            deadline=datetime(2024, 4, 30),
            priority="High",
            project=self.project,
        )
        self.task_create_frontend_architecture = Task.objects.create(
            name="Create frontend architecture",
            deadline=datetime(2024, 4, 30),
            priority="High",
            project=self.project,
        )
        self.task_create_backend_architecture = Task.objects.create(
            name="Create backend architecture",
            deadline=datetime(2024, 4, 30),
            priority="High",
            project=self.project,
        )

        self.task_create_db_structure.assignees.set((self.worker_tony,))
        self.task_create_frontend_architecture.assignees.set((self.worker_tony,))
        self.task_create_backend_architecture.assignees.set((self.worker_tony,))

    def test_should_return_task_only_related_to_user(self) -> None:
        tasks = get_user_tasks(self.worker_tony)

        for task in tasks:
            self.assertIn(self.worker_tony, task.assignees.all())

    def test_should_return_tasks_filtered_by_name_if_name_provided(self) -> None:
        task_name = "backend"

        tasks = get_user_tasks(self.worker_tony, name=task_name)

        for task in tasks:
            self.assertIn(task_name.lower(), task.name.lower())

    def test_should_return_not_completed_tasks_if_is_completed_is_false(self) -> None:
        tasks = get_user_tasks(self.worker_tony, is_completed=False)

        for task in tasks:
            self.assertEqual(task.is_completed, False)

    def test_should_return_completed_tasks_if_is_completed_is_true(self) -> None:
        tasks = get_user_tasks(self.worker_tony, is_completed=True)

        for task in tasks:
            self.assertEqual(task.is_completed, True)
