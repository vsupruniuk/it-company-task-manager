from django.contrib.auth import get_user_model


def update_user(
    user_id: int,
    email: str = None,
    username: str = None,
    first_name=None,
    last_name: str = None,
) -> get_user_model():
    user = get_user_model().objects.get(id=user_id)

    if email:
        user.email = email

    if username:
        user.username = username

    if first_name:
        user.first_name = first_name

    if last_name:
        user.last_name = last_name

    user.save()

    return user
