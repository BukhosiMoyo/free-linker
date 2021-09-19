from django.urls import path
from .views import (HomeView, 
                    LinkProjectView, 
                    ProjectListView, 
                    LinkCreateView, 
                    LinkUpdateView,
                    ProjectCreateView,
                    ProjectUpdateView,
                    ProjectDeleteView,
                    )

urlpatterns = [
    path("", HomeView, name='home'),
    path("projects/", ProjectListView, name="project-list"),
    path("projects/create", ProjectCreateView, name="project-create"),
    path("<str:projects>/update", ProjectUpdateView, name="project-update"),
    path("<str:projects>/delete", ProjectDeleteView, name="project-delete"),
    path("<slug:projects>/", LinkProjectView , name='projects'),
    path("<slug:projects>/create/", LinkCreateView, name="link-create"),
    path("<slug:projects>/update/<slug:pk>", LinkUpdateView, name="link-update"),
]