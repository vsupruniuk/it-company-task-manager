from django.test import TestCase

from manager.models import Team, Position
from manager.services import create_position_for_team


class CreatePositionForTeamTests(TestCase):
    def setUp(self) -> None:
        self.team = Team.objects.create(name="Avengers")

    def test_should_create_position_with_provided_name_and_team_id(self) -> None:
        name = "Developer"

        create_position_for_team(team_id=self.team.id, name=name)

        position = Position.objects.get(name=name)

        self.assertEqual(position.name, name)
        self.assertEqual(position.team, self.team)
