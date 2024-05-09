from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from manager.services import get_projects_with_tasks


@login_required
def index(request: HttpRequest) -> HttpResponse:
    project_name = request.GET.get("project-name")

    projects = get_projects_with_tasks(project_name)

    paginator = Paginator(projects, 5)
    page_number = request.GET.get("page")

    try:
        projects = paginator.page(page_number)
    except PageNotAnInteger:
        projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)

    context = {
        "segment": ["index", "search"],
        "page_obj": projects,
        "is_paginated": paginator.num_pages > 1,
        "search_value": project_name if project_name else "",
        "search_name": "project-name",
        "search_placeholder": "Search projects",
        "user": request.user,
    }

    return render(request=request, template_name="manager/index.html", context=context)
