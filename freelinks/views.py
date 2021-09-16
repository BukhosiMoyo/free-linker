from django.shortcuts import render, redirect
from .models import Link, LinkProject
from .forms import LinkCreateForm, ProjectCreateForm
from django.contrib.auth.decorators import login_required


def HomeView(request):
    return render(request, "freelinks/home.html")


@login_required(login_url='/login/')
def LinkProjectView(request, projects):
    project_links = Link.objects.filter(project__slug=projects)
    my_project = LinkProject.objects.get(project_name=projects)
    form = LinkCreateForm()
    
    if request.method == "POST":
        form = LinkCreateForm(request.POST)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.project = my_project
            my_form.save()
        return redirect("/projects") 
    
    context = {
        "project": projects,
        "project_links": project_links,
        "form": form
    }
    
    return render(request, "freelinks/projects.html", context)


@login_required(login_url='/login/')
def ProjectListView(request):
    projects = LinkProject.objects.all()
    form = ProjectCreateForm()
    
    if request.method == 'POST':
        form = ProjectCreateForm(request.POST)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.slug = my_form.project_name            
            my_form.save()
        return redirect("/projects")
    
    context = {
        'projects': projects,
        "form":form
        }
    
    return render(request, "freelinks/project-list.html", context)




