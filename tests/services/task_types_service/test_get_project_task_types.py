from datetime import date

from django.test import TestCase

from manager.models import Project, TaskType
from manager.services import get_project_task_types


class GetProjectTaskTypesTests(TestCase):
    def setUp(self) -> None:
        self.project_youtube = Project.objects.create(
            name="YouTube", start_date=date(2024, 1, 1), budget=100_000_000
        )
        self.project_twitch = Project.objects.create(
            name="Twitch", start_date=date(2024, 1, 1), budget=100_000_000
        )

        TaskType.objects.create(name="Feature", project=self.project_youtube)
        TaskType.objects.create(name="Bugfix", project=self.project_youtube)
        TaskType.objects.create(name="Testing", project=self.project_twitch)

    def test_should_return_task_types_only_for_specific_project(self) -> None:
        task_types = get_project_task_types(self.project_youtube.id)

        for task_type in task_types:
            self.assertEqual(task_type.project, self.project_youtube)

    def test_should_filter_task_types_by_name_if_name_provided(self) -> None:
        task_types = get_project_task_types(self.project_youtube.id, task_name="fea")

        for task_type in task_types:
            self.assertIn("fea", task_type.name.lower())
