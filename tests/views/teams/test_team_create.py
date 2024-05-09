from datetime import date

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from manager.models import Project, Team


class PublicTeamCreateTests(TestCase):
    def setUp(self) -> None:
        self.url = reverse("manager:team-create")

    def test_team_create_login_required(self) -> None:
        res = self.client.get(self.url)

        self.assertEqual(res.status_code, 302)
        self.assertEqual("/accounts/login/?next=/teams/create/", res.url)


class PrivateTeamCreateTests(TestCase):
    def setUp(self) -> None:
        self.url = reverse("manager:team-create")

        self.user = get_user_model().objects.create_user(
            first_name="Admin",
            last_name="User",
            username="admin",
            password="Qwerty12345!",
        )

        self.client.force_login(self.user)

        self.team_lead = get_user_model().objects.create_user(
            first_name="Tony",
            last_name="Stark",
            username="t.stark",
            password="Qwerty12345!",
        )
        self.project = Project.objects.create(
            name="YouTube", start_date=date(2024, 1, 1), budget=100_000_000
        )

    def test_should_create_team(self) -> None:
        form_data = {
            "name": "Avengers",
            "team_lead": self.team_lead.id,
            "projects": self.project.id,
        }

        self.client.post(self.url, data=form_data)

        created_team = Team.objects.get(name=form_data["name"])

        self.assertEqual(created_team.name, form_data.get("name"))
        self.assertEqual(created_team.team_lead.id, form_data.get("team_lead"))

    def test_should_use_proper_template(self) -> None:
        res = self.client.get(self.url)

        self.assertTemplateUsed(res, "manager/team_form.html")
