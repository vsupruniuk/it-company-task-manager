from .index import index
from .profile import profile
from .my_tasks import my_tasks

from .projects.project_list import ProjectListView
from .projects.project_detail import ProjectDetailView
from .projects.project_create import ProjectCreateView
from .projects.project_update import ProjectUpdateView
from .projects.project_delete import ProjectDeleteView

from .project_task_list import ProjectTaskListView
from .project_task_detail import ProjectTaskDetailView
from .project_task_update import ProjectTaskUpdateView
from .project_task_delete import ProjectTaskDeleteView

from .team_list import TeamListView

from .worker_list import WorkerListView

from .tags.tag_list import TagListView

from .task_types.task_type_list import TaskTypeListView
from .task_types.task_type_detail import TaskTypeDetailView
from .task_types.task_type_create import TaskTypeCreateView
from .task_types.task_type_update import TaskTypeUpdateView
from .task_types.task_type_delete import TaskTypeDeleteView
