from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from apps.jobs import views


urlpatterns = patterns('',
                       url(r'^$', views.IndexView.as_view(), name='index'),
                       url(r'^jobs/(?P<pk>\d+)/$', views.JobView.as_view(), name='job_detail'),
                       url(r'^team/(?P<pk>.*)/$', views.TeamView.as_view(), name='team_detail'),
                       url(r'^teams/$', views.TeamList.as_view(), name='team_list'),
                       url(r'^team/add_team', login_required(views.CreateTeamView.as_view()), name='add_team'),
                       url(r'^team/add_job', login_required(views.CreateJobView.as_view()), name='add_job'),
)