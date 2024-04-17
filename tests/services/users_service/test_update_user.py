from django.contrib.auth import get_user_model
from django.test import TestCase

from manager.services import update_user


class GetUserTests(TestCase):
    def setUp(self) -> None:
        self.worker_tony = get_user_model().objects.create(
            first_name="Tony",
            last_name="Stark",
            username="t.stark",
            email="tony@avanger.com",
            password="Qwerty12345!",
        )

    def test_should_update_first_name(self) -> None:
        user_id = self.worker_tony.id
        new_first_name = "Bruce"

        user = update_user(user_id, first_name=new_first_name)

        self.assertEqual(user.first_name, new_first_name)

    def test_should_update_last_name(self) -> None:
        user_id = self.worker_tony.id
        new_last_name = "Banner"

        user = update_user(user_id, last_name=new_last_name)

        self.assertEqual(user.last_name, new_last_name)

    def test_should_update_username(self) -> None:
        user_id = self.worker_tony.id
        new_username = "b.banner"

        user = update_user(user_id, username=new_username)

        self.assertEqual(user.username, new_username)

    def test_should_update_email(self) -> None:
        user_id = self.worker_tony.id
        new_email = "bruce@avenger.mail"

        user = update_user(user_id, email=new_email)

        self.assertEqual(user.email, new_email)
