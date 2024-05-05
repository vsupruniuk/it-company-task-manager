from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from manager.models import Team
from manager.services import get_teams


class PublicTeamsViewTests(TestCase):
    def setUp(self) -> None:
        self.url = reverse("manager:team-list")

    def test_login_required(self) -> None:
        res = self.client.get(self.url)

        self.assertEqual(res.status_code, 302)
        self.assertEqual(res.url, "/accounts/login/?next=/teams/")


class PrivateTeamsViewTests(TestCase):
    def setUp(self) -> None:
        self.url = reverse("manager:team-list")
        self.user = get_user_model().objects.create_user(
            first_name="Admin",
            last_name="User",
            username="admin",
            password="Qwerty12345!",
        )

        self.client.force_login(self.user)

        Team.objects.create(name="Avengers")
        Team.objects.create(name="Tanos team")
        Team.objects.create(name="Justice League")
        Team.objects.create(name="X-Men")
        Team.objects.create(name="Fantastic Four")
        Team.objects.create(name="Guardians of the Galaxy")
        Team.objects.create(name="The Incredibles")
        Team.objects.create(name="The Avengers")
        Team.objects.create(name="The Defenders")
        Team.objects.create(name="The Suicide Squad")
        Team.objects.create(name="The X-Force")

    def test_should_display_list_of_teams(self) -> None:
        teams = get_teams()

        res = self.client.get(self.url)

        self.assertEqual(list(res.context["team_list"]), list(teams)[:10])

    def test_should_display_list_of_teams_with_pagination(self) -> None:
        teams = get_teams()

        res = self.client.get(self.url + "?page=2")

        self.assertEqual(list(res.context["team_list"]), list(teams)[10:])

    def test_should_display_list_of_teams_with_search(self) -> None:
        teams = get_teams(name="Tanos")

        res = self.client.get(self.url + "?team-name=Tanos")

        self.assertEqual(list(res.context["team_list"]), list(teams)[:1])

    def test_should_use_proper_template(self) -> None:
        res = self.client.get(self.url)

        self.assertTemplateUsed(res, "manager/team_list.html")
