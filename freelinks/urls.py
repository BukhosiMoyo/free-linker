from django.urls import path
from .views import HomeView, LinkProjectView, ProjectListView, LinkCreateView, LinkUpdateView

urlpatterns = [
    path("", HomeView, name='home'),
    path("projects/", ProjectListView, name="project-list"),
    path("<slug:projects>/", LinkProjectView , name='projects'),
    path("<slug:projects>/create/", LinkCreateView, name="link-create"),
    path("<slug:projects>/update/<str:pk>", LinkUpdateView, name="link-update")
]