from django.db.models import QuerySet

from manager.models import Tag


def get_project_tags(project_id: int, tag_name: str | None = None) -> QuerySet[Tag]:
    queryset = Tag.objects.select_related("project").filter(project_id=project_id)

    if tag_name:
        queryset = queryset.filter(name__icontains=tag_name)

    return queryset


def get_tag_with_project(tag_id: int) -> Tag:
    return Tag.objects.select_related("project").get(id=tag_id)


def create_tag_for_project(project_id: int, name: str) -> None:
    Tag.objects.create(name=name, project_id=project_id)
