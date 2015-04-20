from django.contrib import admin
from .models import *

# Register your models here.

class ProjectGroup(admin.ModelAdmin):

    pass


class ProjectAdmin(admin.ModelAdmin):

    pass


admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectMeta, ProjectGroup)
