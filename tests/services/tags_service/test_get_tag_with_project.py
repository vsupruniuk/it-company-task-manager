from datetime import date

from django.test import TestCase

from manager.models import Project, Tag
from manager.services import get_tag_with_project


class GetTagWithProjectTests(TestCase):
    def setUp(self) -> None:
        self.project = Project.objects.create(
            name="YouTube", start_date=date(2024, 1, 1), budget=100_000_000
        )

        self.tag = Tag.objects.create(name="backend", project=self.project)

    def test_should_return_tag_by_id(self) -> None:
        tag = get_tag_with_project(self.tag.id)

        self.assertEqual(tag.name, "backend")
        self.assertEqual(tag.project, self.project)
