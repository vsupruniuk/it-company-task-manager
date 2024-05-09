from django.contrib.auth import get_user_model
from django.test import TestCase

from manager.services import get_workers


class GetWorkersTests(TestCase):
    def setUp(self) -> None:
        get_user_model().objects.create_user(
            first_name="Tony",
            last_name="Stark",
            username="t.stark",
            password="Qwerty12345!",
        )

        get_user_model().objects.create_user(
            first_name="Steve",
            last_name="Rogers",
            username="s.rogers",
            password="Qwerty12345!",
        )

    def test_should_return_all_workers_uf_username_not_provided(self) -> None:
        all_workers = get_user_model().objects.all()
        workers = get_workers()

        self.assertEqual(list(all_workers), list(workers))

    def test_should_filter_workers_by_username_if_username_provided(self) -> None:
        workers = get_workers(username="stark")

        for worker in workers:
            self.assertIn("stark", worker.username.lower())
