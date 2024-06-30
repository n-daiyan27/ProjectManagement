from django import forms
from django.contrib.auth.models import User
from .models import Project, Task

class ProjectForm(forms.ModelForm):
    members = forms.ModelMultipleChoiceField(queryset=User.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Project
        fields = ['name', 'description', 'members']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'assigned_to']

    def __init__(self, *args, **kwargs):
        project = kwargs.pop('project', None)
        super().__init__(*args, **kwargs)
        if project:
            self.fields['assigned_to'].queryset = project.members.all()

class TaskAssignmentForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['assigned_to']

    def __init__(self, *args, **kwargs):
        project = kwargs.pop('project', None)
        super().__init__(*args, **kwargs)
        if project:
            self.fields['assigned_to'].queryset = project.members.all()
