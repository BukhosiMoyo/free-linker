from django.urls import path
from .views import HomeView, LinkProjectView

urlpatterns = [
    path("", HomeView, name='home'),
    path("<str:projects>", LinkProjectView, name='projects'),
]