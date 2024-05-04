from .index import index
from .profile import profile
from .my_tasks import my_tasks

from .projects.project_list import ProjectListView
from .projects.project_detail import ProjectDetailView
from .projects.project_create import ProjectCreateView
from .projects.project_update import ProjectUpdateView
from .projects.project_delete import ProjectDeleteView

from .tasks.task_list import TaskListView
from .tasks.task_create import TaskCreateView
from .tasks.task_update import TaskUpdateView
from .tasks.task_detail import TaskDetailView
from .tasks.task_delete import TaskDeleteView

from .workers.worker_list import WorkerListView
from .workers.worker_detail import WorkerDetailView
from .workers.worker_create import WorkerCreateView

from .tags.tag_list import TagListView
from .tags.tag_detail import TagDetailView
from .tags.tag_create import TagCreateView
from .tags.tag_update import TagUpdateView
from .tags.tag_delete import TagDeleteView

from .task_types.task_type_list import TaskTypeListView
from .task_types.task_type_detail import TaskTypeDetailView
from .task_types.task_type_create import TaskTypeCreateView
from .task_types.task_type_update import TaskTypeUpdateView
from .task_types.task_type_delete import TaskTypeDeleteView

from .team_list import TeamListView
