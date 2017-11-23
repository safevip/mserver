# Create your views here.
from django.views.generic import ListView,TemplateView

from project.models import Project


# 项目
class ProjectList(ListView):
    template_name = "project/projectlist.html"
    model = Project
    context_object_name = "projectList"


class ProjectAdd(TemplateView):
    template_name = "project/add.html"


class ProjectDetail:
    pass


# 任务
# 项目的任务列表
class TaskList:
    pass


# 触发任务
class TaskInvoke:
    pass


# 任务触发历史
class TaskRecord:
    pass


class TaskRecordDetail:
    pass
