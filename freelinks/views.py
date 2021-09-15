from django.shortcuts import render
from .models import Link


def HomeView(request):
    return render(request, "freelinks/home.html")


def LinkProjectView(request, projects):
    project_links = Link.objects.filter(project__slug=projects)
    
    context = {
        "project": projects,
        "project_links": project_links
    }
    
    return render(request, "freelinks/projects.html", context)