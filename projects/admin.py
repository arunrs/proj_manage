from django.contrib import admin
from .models import *

# Register your models here.


class DomainAdmin(admin.ModelAdmin):

    list_display = ('name', 'description')


class SprintInline(admin.StackedInline):

    model = Sprint
    max_num = 1


class ProjectAdmin(admin.ModelAdmin):

    list_display = ('name', \
                    'client_name',
                    'domain',
                    'start_date', 'end_date',
                    'actual_end_date',
                    'created_on')

    search_fields = ('name', )

    list_filter = ('domain', )

    inlines = [SprintInline, ]
        

class ProjectGroup(admin.ModelAdmin):

    pass


class SprintAdmin(admin.ModelAdmin):

    list_display = ('name', 'version', \
                    'project_ref',\
                    'freezed_sprint',\
                    'tagged',
                    'start_date',
                    'end_date',
                    'actual_end_date',
                    'created_on'
                    )

    list_filter = ('freezed_sprint', )


class TaskAdmin(admin.ModelAdmin):

    list_display = ('name',
                    'sprint',
                    'technology',
                    'allocated_user',
                    'additional',
                    'closed',
                    'estimated_hrs',
                    'start_date',
                    'end_date',
                    )

    list_filter = ('closed', 'additional')
    

class BugAdmin(admin.ModelAdmin):

    list_display = ('name',
                    'page_url',
                    'reopened',
                    'related_task',
                    'start_date',
                    'end_date',
                    'closed')

        
    
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectMeta, ProjectGroup)
admin.site.register(Domian, DomainAdmin)
admin.site.register(Sprint, SprintAdmin)
admin.site.register(Task, TaskAdmin)

