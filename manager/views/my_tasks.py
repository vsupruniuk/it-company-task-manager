from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def my_tasks(request: HttpRequest) -> HttpResponse:
    context = {
        "user": request.user,
    }

    return render(
        request=request, template_name="manager/my_tasks.html", context=context
    )
