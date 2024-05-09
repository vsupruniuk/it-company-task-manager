from datetime import date

from django.test import TestCase

from manager.models import Project, Tag
from manager.services import create_tag_for_project


class CreateTagForProjectTests(TestCase):
    def setUp(self) -> None:
        self.project = Project.objects.create(
            name="YouTube", start_date=date(2024, 1, 1), budget=100_000_000
        )

    def test_should_create_tag_with_provided_name_and_project_id(self) -> None:
        name = "backend"

        create_tag_for_project(project_id=self.project.id, name=name)

        tag = Tag.objects.get(name=name)

        self.assertEqual(tag.name, name)
        self.assertEqual(tag.project, self.project)
