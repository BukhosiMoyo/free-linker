from django.shortcuts import render, redirect
from .models import Link, LinkProject
from django.views.generic import ListView
from .forms import LinkCreateForm


def HomeView(request):
    return render(request, "freelinks/home.html")


def LinkProjectView(request, projects):
    project_links = Link.objects.filter(project__slug=projects)
    my_project = LinkProject.objects.get(project_name=projects)
    form = LinkCreateForm()
    
    if request.method == "POST":
        form = LinkCreateForm(request.POST)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.project = my_project
            
            # TODO BUG the form is not updating the project field
            my_form.save()
        return redirect("/projects") 
    
    context = {
        "project": projects,
        "project_links": project_links,
        "form": form
    }
    
    return render(request, "freelinks/projects.html", context)


class ProjectListView(ListView):
    queryset = LinkProject.objects.all()
    model = LinkProject
    template_name = "freelinks/project-list.html"
    context_object_name = "projects"


