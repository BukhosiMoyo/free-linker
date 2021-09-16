from django.shortcuts import render, redirect
from .models import Link, LinkProject
from django.views.generic import ListView
from .forms import LinkCreateForm


def HomeView(request):
    return render(request, "freelinks/home.html")


def LinkProjectView(request, projects):
    project_links = Link.objects.filter(project__slug=projects)
    form = LinkCreateForm()
    
    if request.method == "POST":
        form = LinkCreateForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data["project"])
            form.save(commit=False)
            form.cleaned_data["project"] = projects
            print(form.cleaned_data["project"])
            # TODO BUG the form is not updating the project field
            form.save()
            print(form.cleaned_data)
        return redirect("/") 
    
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


