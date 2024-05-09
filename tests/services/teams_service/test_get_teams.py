from django.test import TestCase

from manager.models import Team
from manager.services import get_teams


class GetTeamsTests(TestCase):
    def setUp(self) -> None:
        Team.objects.create(name="Avengers")
        Team.objects.create(name="Tanos team")

    def test_should_return_all_teams_if_name_not_provided(self) -> None:
        all_teams = Team.objects.all()
        teams = get_teams()

        self.assertEqual(list(all_teams), list(teams))

    def test_should_filter_teams_by_name_if_name_provided(self) -> None:
        teams = get_teams(name="tanos")

        for team in teams:
            self.assertIn("tanos", team.name.lower())
