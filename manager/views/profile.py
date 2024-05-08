from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from manager.services import update_user


@login_required
def profile(request: HttpRequest) -> HttpResponse:
    user = request.user

    if request.method == "POST":
        user = update_user(
            user_id=request.user.id,
            email=request.POST.get("email"),
            username=request.POST.get("username"),
            first_name=request.POST.get("first_name"),
            last_name=request.POST.get("last_name"),
        )

    context = {
        "user": user,
    }

    return render(
        request=request, template_name="manager/profile.html", context=context
    )
