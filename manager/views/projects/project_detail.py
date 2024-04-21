from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from manager.models import Project


class ProjectDetailView(LoginRequiredMixin, generic.DetailView):
    model = Project
