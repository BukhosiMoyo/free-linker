from django.shortcuts import render, redirect
from .models import Link, LinkProject
from .forms import LinkCreateForm, ProjectCreateForm


def HomeView(request):
    return render(request, "freelinks/home.html")


def LinkProjectView(request, projects):
    """Links"""
    project_links = Link.objects.filter(project__slug=projects)
    
    context = {
        "pl": projects,
        "project_links": project_links,
        
    }
    
    return render(request, "freelinks/projects.html", context)


def LinkCreateView(request, projects):
    """Link Create"""
    my_project = LinkProject.objects.get(project_name=projects)
    project_links = LinkProject.objects.get(slug=projects)
    form = LinkCreateForm()
    
    if request.method == "POST":
        form = LinkCreateForm(request.POST)
        print(project_links)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.project = my_project
            my_form.save()
        return redirect("/projects")
    
    context = {
        "form": form,
        "project_links": project_links,
    }
    
    return render(request, "freelinks/link-create.html", context)



def LinkUpdateView(request, projects, pk):
    """Link Update"""
    my_project = LinkProject.objects.get(project_name=projects)
    project_links = LinkProject.objects.get(slug=projects)
    mylink = Link.objects.get(id=pk)
    form = LinkCreateForm()
    
    if request.method == "POST":
        form = LinkCreateForm(request.POST)
        print(project_links)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.project = my_project
            my_form.save()
        return redirect("/projects")
    
    context = {
        "form": form,
        "project_links": project_links,
        "pk":pk,
    }
    
    return render(request, "freelinks/link-create.html", context)





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
