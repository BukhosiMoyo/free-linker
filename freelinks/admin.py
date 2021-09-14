from django.contrib import admin
from .models import Link, LinkProject, Profile


class LinkAdmin(admin.ModelAdmin):
    list_display = ["name", "project",]
    
admin.site.register(Link, LinkAdmin)


admin.site.register(LinkProject)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "user"]
    
admin.site.register(Profile, ProfileAdmin)