from django.forms import ModelForm

from project.models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        # fields = ['name', 'desc', 'type', 'script', 'project']
        # fileds表示model要转换到form的字段
        fields = ['name', 'desc', 'type', 'script']
