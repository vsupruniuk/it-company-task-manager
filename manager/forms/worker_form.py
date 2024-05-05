from django.contrib.auth.forms import UserCreationForm

from manager.models import Worker


class WorkerForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "team",
        )
