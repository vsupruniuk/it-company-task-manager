from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def profile(request: HttpRequest) -> HttpResponse:
    context = {
        "user": request.user,
    }

    return render(
        request=request, template_name="manager/profile.html", context=context
    )
