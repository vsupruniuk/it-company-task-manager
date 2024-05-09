from django.test import TestCase

from manager.models import Team
from manager.services import get_team


class GetTeamTests(TestCase):
    def setUp(self) -> None:
        self.team = Team.objects.create(name="Avengers")

    def test_should_return_task_by_id(self) -> None:
        team = get_team(self.team.id)

        self.assertEqual(team, self.team)
