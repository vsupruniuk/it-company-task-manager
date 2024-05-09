from datetime import datetime

from django.test import TestCase

from manager.models import Project
from manager.services import get_all_projects


class GetAllProjectsTests(TestCase):
    def setUp(self) -> None:
        self.project_youtube = Project.objects.create(
            name="You Tube", start_date=datetime(2024, 1, 1), budget=100_000_000
        )
        self.project_twitch = Project.objects.create(
            name="Twitch", start_date=datetime(2024, 1, 1), budget=50_000_000
        )

    def test_should_return_all_projects_if_name_not_provided(self) -> None:
        all_projects = Project.objects.all()
        projects = get_all_projects()

        self.assertEqual(list(all_projects), list(projects))

    def test_should_return_filtered_projects_if_name_provided(self) -> None:
        all_projects = Project.objects.filter(name__icontains="you tube")
        projects = get_all_projects("you tube")

        self.assertEqual(list(all_projects), list(projects))
