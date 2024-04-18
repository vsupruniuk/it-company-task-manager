from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from manager.services import get_user_tasks


def my_tasks(request: HttpRequest) -> HttpResponse:
    task_name = request.GET.get("task-name")
    is_completed = (
        request.GET.get("is_completed") == "True"
        if request.GET.get("is_completed")
        else None
    )

    tasks = get_user_tasks(user=request.user, name=task_name, is_completed=is_completed)

    paginator = Paginator(tasks, 10)
    page_number = request.GET.get("page")

    try:
        tasks = paginator.page(page_number)
    except PageNotAnInteger:
        tasks = paginator.page(1)
    except EmptyPage:
        tasks = paginator.page(paginator.num_pages)

    context = {
        "segment": ["search"],
        "search_name": "task-name",
        "search_placeholder": "Search tasks",
        "is_completed": is_completed if isinstance(is_completed, bool) else None,
        "search_value": task_name if task_name else "",
        "page_obj": tasks,
        "is_paginated": paginator.num_pages > 1,
    }

    return render(
        request=request, template_name="manager/my_tasks.html", context=context
    )
