from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from manager.models import Team


class PublicTeamDeleteTests(TestCase):
    def setUp(self) -> None:
        self.url = reverse("manager:team-delete", kwargs={"pk": 1})

    def test_team_delete_login_required(self) -> None:
        res = self.client.get(self.url)

        self.assertEqual(res.status_code, 302)
        self.assertEqual("/accounts/login/?next=/teams/1/delete/", res.url)


class PrivateTeamDeleteTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            first_name="Admin",
            last_name="User",
            username="admin",
            password="Qwerty12345!",
        )

        self.client.force_login(self.user)

        self.team = Team.objects.create(name="Avengers")

        self.url = reverse("manager:team-delete", kwargs={"pk": self.team.pk})

    def test_should_delete_team(self) -> None:
        self.client.post(self.url)

        team = Team.objects.filter(name="Avengers")

        self.assertEqual(list(team), [])

    def test_should_use_proper_template(self) -> None:
        res = self.client.get(self.url)

        self.assertTemplateUsed(res, "manager/team_confirm_delete.html")
