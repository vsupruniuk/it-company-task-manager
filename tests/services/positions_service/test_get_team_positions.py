from django.test import TestCase

from manager.models import Team, Position
from manager.services import get_team_positions


class GetTeamPositionsTests(TestCase):
    def setUp(self) -> None:
        self.team_avengers = Team.objects.create(name="Avengers")
        self.team_thanos = Team.objects.create(name="Thanos team")

        Position.objects.create(name="Developer", team=self.team_avengers)
        Position.objects.create(name="QA", team=self.team_avengers)
        Position.objects.create(name="Developer", team=self.team_thanos)

    def test_should_return_positions_only_for_specific_team(self) -> None:
        positions = get_team_positions(self.team_avengers.id)

        for position in positions:
            self.assertEqual(position.team, self.team_avengers)

    def test_should_filter_positions_by_name_if_name_provided(self) -> None:
        positions = get_team_positions(self.team_avengers.id, position_name="qa")

        for position in positions:
            self.assertIn("qa", position.name.lower())
