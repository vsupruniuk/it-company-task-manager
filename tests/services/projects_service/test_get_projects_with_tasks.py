from datetime import datetime

from django.test import TestCase

from manager.models import Project


class GetProjectsWithTasksTests(TestCase):
    def setUp(self) -> None:
        self.project_you_tube = Project.objects.create(
            name="You Tube", start_date=datetime(2024, 1, 1), budget=100_000_000
        )
        self.project_twitch = Project.objects.create(
            name="Twitch", start_date=datetime(2024, 1, 1), budget=150_000_000
        )
        self.project_instagram = Project.objects.create(
            name="Instagram", start_date=datetime(2024, 1, 1), budget=125_000_000
        )
        self.project_facebook = Project.objects.create(
            name="Facebook", start_date=datetime(2024, 1, 1), budget=200_000_000
        )

    def test_true(self) -> None:
        self.assertTrue(True)
