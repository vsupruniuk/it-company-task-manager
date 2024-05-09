from django.contrib.auth import get_user_model
from django.test import TestCase

from manager.services import get_worker


class GetFullTaskTests(TestCase):
    def setUp(self) -> None:
        self.worker = get_user_model().objects.create_user(
            first_name="Admin",
            last_name="User",
            username="admin",
            password="Qwerty12345!",
        )

    def test_should_return_task_by_id(self) -> None:
        worker = get_worker(self.worker.id)

        self.assertEqual(worker, self.worker)
