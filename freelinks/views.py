from django.shortcuts import render, redirect
from .models import Link, LinkProject
from .forms import LinkCreateForm, ProjectCreateForm

from django.utils.text import slugify   # Importing this to be able to slugify from view.py


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
    my_project = LinkProject.objects.get(slug=projects) # the url contains the slug not the project name itself, so we have get the Link Project from the database using the slug
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
    
    
    if request.method == 'POST':
        form = ProjectCreateForm(request.POST)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.slug = my_form.project_name     
            my_form.save()
        return redirect("/projects")
    
    context = {
        'projects': projects,
        }
    
    return render(request, "freelinks/project-list.html", context)


def ProjectCreateView(request):
    """"Create a Project"""
    form = ProjectCreateForm()
    
    if request.method == 'POST':
        form = ProjectCreateForm(request.POST)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.slug = slugify(my_form.project_name )     
            my_form.save()
        return redirect("/projects")
    
    context = {
        "form":form
        }
    
    return render(request, "freelinks/project-create.html", context)

# In the admin panel slugs are auto generated for every Link Project created,to update it we need to create a new slug for the updated  Link Project 


def ProjectUpdateView(request, projects):
    my_project = LinkProject.objects.get(slug=projects)
    """"Project Update"""
    form = ProjectCreateForm(instance=my_project)
    
    if request.method == 'POST':
        form = ProjectCreateForm(request.POST, instance=my_project)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.slug = slugify(my_form.project_name)      
            my_form.save()
        return redirect("/projects")
    
    context = {
        "form":form
        }
    
    return render(request, "freelinks/project-update.html", context)


def ProjectDeleteView(request, projects):
    my_project = LinkProject.objects.get(project_name=projects)
    """"Project Update"""
    
    if request.method == 'POST':
        my_project.delete()
        return redirect("/projects")
    
    context = {
        "my_project": my_project
        }
    
    return render(request, "freelinks/project-delete.html", context)