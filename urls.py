from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^', include('apps.jobs.urls', namespace='jobs')),
                       url(r'^accounts/', include('django.contrib.auth.urls')),
                       url(r'^accounts/', include('apps.account.urls', namespace='account')),
)
