from django.views import generic

from manager.models import Team


class TeamListView(generic.ListView):
    model = Team
    context_object_name = "team_list"
