from datetime import date, datetime

from django.test import TestCase

from manager.models import Project, Task
from manager.services import get_full_task


class GetFullTaskTests(TestCase):
    def setUp(self) -> None:
        self.project = Project.objects.create(
            name="YouTube", start_date=date(2024, 1, 1), budget=100_000_000
        )

        self.task = Task.objects.create(
            name="Create DB structure",
            deadline=datetime(2024, 5, 10),
            project=self.project,
            priority="high",
        )

    def test_should_return_task_by_id(self) -> None:
        task = get_full_task(self.task.id)

        self.assertEqual(task, self.task)
