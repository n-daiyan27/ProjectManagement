from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Project, Task
from .forms import ProjectForm, TaskForm, TaskAssignmentForm

@login_required
def project_list(request):
    projects = Project.objects.filter(members=request.user)
    return render(request, 'main/project_list.html', {'projects': projects})

@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    tasks = project.tasks.all()
    return render(request, 'main/project_detail.html', {'project': project, 'tasks': tasks})

@login_required
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm()
    return render(request, 'main/project_form.html', {'form': form})

@login_required
def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'main/project_form.html', {'form': form})

@login_required
def task_create(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, project=project)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = TaskForm(project=project)
    return render(request, 'main/task_form.html', {'form': form, 'project': project})

@login_required
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    project = task.project
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task, project=project)
        if form.is_valid():
            form.save()
            return redirect('project_detail', pk=task.project.pk)
    else:
        form = TaskForm(instance=task, project=project)
    return render(request, 'main/task_form.html', {'form': form, 'task': task, 'project': project})


@login_required
def task_assign(request, pk):
    task = get_object_or_404(Task, pk=pk)
    project = task.project
    if request.method == 'POST':
        form = TaskAssignmentForm(request.POST, instance=task, project=project)
        if form.is_valid():
            form.save()
            return redirect('project_detail', pk=task.project.pk)
    else:
        form = TaskAssignmentForm(instance=task, project=project)
    return render(request, 'main/task_assign_form.html', {'form': form, 'task': task})
