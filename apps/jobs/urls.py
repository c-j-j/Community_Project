from django.conf.urls import patterns, url
from apps.jobs.views import job_details

urlpatterns = patterns('apps.jobs.views',
                       url(r'^$', 'index', name='jobs_home'),
                       url(r'^job_details/(?P<job_id>[\w]+)/$', 'apps.jobs.job_details', name='job_details'),


)