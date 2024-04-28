from datetime import date

from django.test import TestCase

from manager.models import Project, Tag
from manager.services import get_project_tags


class GetProjectTagsTests(TestCase):
    def setUp(self) -> None:
        self.project_youtube = Project.objects.create(
            name="YouTube", start_date=date(2024, 1, 1), budget=100_000_000
        )
        self.project_twitch = Project.objects.create(
            name="Twitch", start_date=date(2024, 1, 1), budget=100_000_000
        )

        Tag.objects.create(name="backend", project=self.project_youtube)
        Tag.objects.create(name="frontend", project=self.project_youtube)
        Tag.objects.create(name="backend", project=self.project_twitch)

    def test_should_return_tags_only_for_specific_project(self) -> None:
        tags = get_project_tags(self.project_youtube.id)

        for tag in tags:
            self.assertEqual(tag.project, self.project_youtube)

    def test_should_filter_tags_by_name_if_name_provided(self) -> None:
        tags = get_project_tags(self.project_youtube.id, tag_name="back")

        for tag in tags:
            self.assertIn("back", tag.name.lower())
