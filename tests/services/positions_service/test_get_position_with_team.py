from django.test import TestCase

from manager.models import Team, Position
from manager.services import get_position_with_team


class GetPositionWithTeamTests(TestCase):
    def setUp(self) -> None:
        self.team = Team.objects.create(name="Avengers")
        self.position = Position.objects.create(name="Developer", team=self.team)

    def test_should_return_position_by_id(self) -> None:
        position = get_position_with_team(self.position.id)

        self.assertEqual(position.name, "Developer")
        self.assertEqual(position.team, self.team)
