from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from manager.models import Project
from manager.services import get_all_projects


class PublicProjectsViewTests(TestCase):
    def setUp(self) -> None:
        self.url = reverse("manager:project-list")

    def test_login_required(self) -> None:
        res = self.client.get(self.url)

        self.assertEqual(res.status_code, 302)
        self.assertEqual(res.url, "/accounts/login/?next=/projects/")


class PrivateProjectsViewTests(TestCase):
    def setUp(self) -> None:
        self.url = reverse("manager:project-list")
        self.user = get_user_model().objects.create_user(
            first_name="Admin",
            last_name="User",
            username="admin",
            password="Qwerty12345!",
        )

        self.client.force_login(self.user)

        self.project_youtube = Project.objects.create(
            name="YouTube video hosting",
            start_date=datetime(2024, 1, 1),
            budget=100_000_000,
        )
        self.projects_twitch = Project.objects.create(
            name="Twitch",
            start_date=datetime(2024, 1, 1),
            budget=50_000_000,
        )
        self.project_netflix = Project.objects.create(
            name="Netflix Originals",
            start_date=datetime(2024, 3, 15),
            budget=200_000_000,
        )
        self.project_spotify = Project.objects.create(
            name="Spotify Podcast Expansion",
            start_date=datetime(2024, 2, 1),
            budget=80_000_000,
        )
        self.project_disney_plus = Project.objects.create(
            name="Disney+ Content Expansion",
            start_date=datetime(2024, 4, 1),
            budget=150_000_000,
        )
        self.project_amazon_prime = Project.objects.create(
            name="Amazon Prime Video Originals",
            start_date=datetime(2024, 2, 15),
            budget=120_000_000,
        )
        self.project_hulu = Project.objects.create(
            name="Hulu Exclusive Series",
            start_date=datetime(2024, 3, 1),
            budget=90_000_000,
        )
        self.project_apple_tv = Project.objects.create(
            name="Apple TV+ Original Films",
            start_date=datetime(2024, 2, 28),
            budget=100_000_000,
        )
        self.project_hbo_max = Project.objects.create(
            name="HBO Max Original Series",
            start_date=datetime(2024, 1, 15),
            budget=130_000_000,
        )
        self.project_facebook_watch = Project.objects.create(
            name="Facebook Watch Original Content",
            start_date=datetime(2024, 3, 5),
            budget=70_000_000,
        )
        self.project_google_play = Project.objects.create(
            name="Google Play Movies & TV",
            start_date=datetime(2024, 4, 10),
            budget=60_000_000,
        )

    def test_should_display_list_of_projects(self) -> None:
        projects = get_all_projects()

        res = self.client.get(self.url)

        self.assertEqual(list(res.context["project_list"]), list(projects)[:10])

    def test_should_display_list_of_projects_with_pagination(self) -> None:
        projects = get_all_projects()

        res = self.client.get(self.url + "?page=2")

        self.assertEqual(list(res.context["project_list"]), list(projects)[10:])

    def test_should_display_list_of_tasks_with_search(self) -> None:
        projects = get_all_projects(name="YouTube")

        res = self.client.get(self.url + "?project-name=YouTube")

        self.assertEqual(list(res.context["project_list"]), list(projects)[:1])

    def test_should_use_proper_template(self) -> None:
        res = self.client.get(self.url)

        self.assertTemplateUsed(res, "manager/project_list.html")
