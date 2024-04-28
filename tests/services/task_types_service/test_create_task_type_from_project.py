from datetime import date

from django.test import TestCase

from manager.models import Project, TaskType
from manager.services import create_task_type_for_project


class CreateTaskTypeForProjectTests(TestCase):
    def setUp(self) -> None:
        self.project = Project.objects.create(
            name="YouTube", start_date=date(2024, 1, 1), budget=100_000_000
        )

    def test_should_create_task_type_with_provided_name_and_project_id(self) -> None:
        name = "Feature"

        create_task_type_for_project(project_id=self.project.id, name=name)

        task_type = TaskType.objects.get(name=name)

        self.assertEqual(task_type.name, name)
        self.assertEqual(task_type.project, self.project)
