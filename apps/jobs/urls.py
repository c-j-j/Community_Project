from django.conf.urls import patterns, url
from apps.jobs import views

urlpatterns = patterns('',
                       url(r'^$', views.IndexView.as_view(), name='index'),
                       url(r'^jobs/(?P<pk>\d+)/$',views.JobView.as_view(), name='detail'),
                       url(r'^team/(?P<slug>[-\w]+)/$',views.TeamView.as_view(), name='team'),
)