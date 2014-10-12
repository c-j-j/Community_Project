from django.contrib import admin

from apps.jobs.models import Job, Team


class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at',)
    search_fields = ('title', 'description')


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'location')
    prepopulated_fields = {'slug': ('name',)}



admin.site.register(Job, JobAdmin)
admin.site.register(Team, TeamAdmin)
