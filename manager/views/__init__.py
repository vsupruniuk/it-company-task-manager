from .index import index
from .profile import profile

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

from .my_tasks import my_tasks
