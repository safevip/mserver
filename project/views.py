# Create your views here.
from django.views.generic import ListView, TemplateView, CreateView, UpdateView
from django.http import HttpResponse, HttpResponseRedirect
from project.models import Project, Task


# 项目
class ProjectList(ListView):
    template_name = "project/projectlist.html"
    model = Project
    context_object_name = "projectList"


class ProjectAdd(CreateView):
    template_name = "project/add.html"
    model = Project
    fields = ['name', 'type', 'desc', 'path', 'package_name', 'on_work']

    def post(self, request):
        name = request.POST.get("name")
        path = request.POST.get("path")
        desc = request.POST.get("desc")
        package = request.POST.get("package")
        type = request.POST.get("projectType")
        p = Project()
        p.name = name
        p.path = path
        p.type = type
        p.desc = desc
        p.package_name = package
        p.on_work = False
        p.save()
        print(">>>>>>>>>" + package + " " + type)
        return HttpResponseRedirect("/project/list")


class ProjectDetail():
    pass


class ProjectEdit(UpdateView):
    pass


# 任务
# 项目的任务列表
class TaskList(ListView):
    template_name = "project/tasklist.html"
    model = Task
    context_object_name = "taskList"

    def get_queryset(self):
        task_list = Task.objects.all()
        return task_list


class TaskAdd:
    pass


class TaskDel:
    pass


class TaskEdit:
    pass


# 触发任务
class TaskInvoke:
    pass


# 任务触发历史
class TaskRecord:
    pass


class TaskRecordDetail:
    pass
