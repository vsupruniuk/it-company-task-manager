from datetime import date

from django.test import TestCase

from manager.models import Project, TaskType
from manager.services import get_task_type_with_project


class GetTaskTypeWithProjectTests(TestCase):
    def setUp(self) -> None:
        self.project = Project.objects.create(
            name="YouTube", start_date=date(2024, 1, 1), budget=100_000_000
        )

        self.task_type_feature = TaskType.objects.create(
            name="Feature", project=self.project
        )

    def test_should_return_task_types_by_id(self) -> None:
        task_type = get_task_type_with_project(self.task_type_feature.id)

        self.assertEqual(task_type, self.task_type_feature)
