from datetime import date

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from manager.models import Team, Project


class PublicTeamDetailTests(TestCase):
    def setUp(self) -> None:
        self.url = reverse("manager:team-detail", kwargs={"pk": 1})

    def test_team_detail_login_required(self) -> None:
        res = self.client.get(self.url)

        self.assertEqual(res.status_code, 302)
        self.assertEqual("/accounts/login/?next=/teams/1/", res.url)


class PrivateTeamDetailTests(TestCase):
    def setUp(self) -> None:
        self.project = Project.objects.create(
            name="YouTube", start_date=date(2924, 1, 1), budget=100_000_000
        )
        self.team_lead = get_user_model().objects.create_user(
            first_name="Tony",
            last_name="Stark",
            username="t.stark",
            password="Qwerty12345!",
        )
        self.team = Team.objects.create(
            name="Avengers-developers", team_lead=self.team_lead
        )
        self.team.projects.set((self.project,))

        self.url = reverse("manager:team-detail", kwargs={"pk": self.team.pk})

        self.user = get_user_model().objects.create_user(
            first_name="Admin",
            last_name="User",
            username="admin",
            password="Qwerty12345!",
        )

        self.client.force_login(self.user)

    def test_should_display_team_details(self) -> None:
        res = self.client.get(self.url)

        self.assertContains(res, self.team.name)
        self.assertContains(res, self.team.team_lead.username)
        self.assertContains(res, self.project.name)

    def test_should_use_proper_template(self) -> None:
        res = self.client.get(self.url)

        self.assertTemplateUsed(res, "manager/team_detail.html")
