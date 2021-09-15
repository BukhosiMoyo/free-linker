from django.urls import path
from .views import HomeView, LinkProjectView, ProjectListView

urlpatterns = [
    path("", HomeView, name='home'),
    path("projects/", ProjectListView.as_view(), name="project-list"),
    path("<slug:projects>/", LinkProjectView , name='projects'),
]