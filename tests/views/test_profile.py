from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class PublicProfileViewTests(TestCase):
    def setUp(self) -> None:
        self.url = reverse("profile")

    def test_login_required(self) -> None:
        res = self.client.get(self.url)

        self.assertEqual(res.status_code, 302)
        self.assertEqual("/accounts/login/?next=/accounts/profile", res.url)


class PrivateProfileViewTests(TestCase):
    def setUp(self) -> None:
        self.url = reverse("profile")
        self.user = get_user_model().objects.create_user(
            first_name="Admin",
            last_name="User",
            username="admin",
            password="Qwerty12345!",
        )

        self.client.force_login(self.user)

    def test_should_display_authorized_user_data(self) -> None:
        res = self.client.get(self.url)

        self.assertContains(res, self.user.first_name)
        self.assertContains(res, self.user.last_name)
        self.assertContains(res, self.user.username)
        self.assertContains(res, self.user.email)

    def test_should_use_proper_template(self) -> None:
        res = self.client.get(self.url)

        self.assertTemplateUsed(res, "manager/profile.html")

    # @patch("manager.services.update_user")
    # def test_should_be_possible_to_send_form_with_updated_user_data(
    #     self, mock_update_user: MagicMock
    # ) -> None:
    #     post_data = {
    #         "first_name": "Bruce",
    #         "last_name": "Banner",
    #         "username": "b.banner",
    #         "email": "bruce@avengers.com",
    #     }
    #
    #     res = self.client.post(self.url, data=post_data)
    #
    #     self.assertEqual(res.status_code, 200)
    #     mock_update_user.assert_called_once()
