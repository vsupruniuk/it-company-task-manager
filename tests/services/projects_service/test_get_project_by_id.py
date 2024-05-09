from datetime import date

from django.test import TestCase

from manager.models import Project
from manager.services import get_project_by_id


class GetProjectByIdTests(TestCase):
    def setUp(self) -> None:
        self.project = Project.objects.create(
            name="YouTube", start_date=date(2024, 1, 1), budget=100_000_000
        )

    def test_should_return_project_by_id(self) -> None:
        task = get_project_by_id(self.project.id)

        self.assertEqual(task, self.project)
