from django.contrib import admin

from apps.jobs.models import Job, Team, JobComment


class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at',)
    search_fields = ('title', 'description')


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'location')


class JobCommentAdmin(admin.ModelAdmin):
    list_display = ('comment', 'user', 'created_at', 'job')



admin.site.register(Job, JobAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(JobComment, JobCommentAdmin)
