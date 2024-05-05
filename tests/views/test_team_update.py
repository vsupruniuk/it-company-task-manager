from datetime import date

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from manager.models import Team, Project


class PublicTeamUpdateTests(TestCase):
    def setUp(self) -> None:
        self.url = reverse("manager:team-update", kwargs={"pk": 1})

    def test_worker_update_login_required(self) -> None:
        res = self.client.get(self.url)

        self.assertEqual(res.status_code, 302)
        self.assertEqual("/accounts/login/?next=/teams/1/update/", res.url)


class PrivateTeamUpdateTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            first_name="Admin",
            last_name="User",
            username="admin",
            password="Qwerty12345!",
        )

        self.client.force_login(self.user)

        self.team = Team.objects.create(name="Avengers")
        self.team_lead = get_user_model().objects.create_user(
            first_name="Tony",
            last_name="Stark",
            username="t.stark",
            password="Qwerty12345!",
        )
        self.project = Project.objects.create(
            name="YouTube", start_date=date(2924, 1, 1), budget=100_000_000
        )

        self.url = reverse("manager:team-update", kwargs={"pk": self.team.pk})

    def test_should_update_worker(self) -> None:
        form_data = {
            "name": "Avengers-developers",
            "team_lead": self.team_lead.id,
            "projects": self.project.id,
        }

        self.client.post(self.url, data=form_data)

        updated_team = Team.objects.get(name=form_data["name"])

        self.assertEqual(updated_team.name, form_data.get("name"))
        self.assertEqual(updated_team.team_lead.id, form_data.get("team_lead"))

    def test_should_use_proper_template(self) -> None:
        res = self.client.get(self.url)

        self.assertTemplateUsed(res, "manager/team_form.html")
