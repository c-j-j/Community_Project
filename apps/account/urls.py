from django.conf.urls import patterns, url
from apps.account import views

urlpatterns = patterns('apps.account.views',
                       url(r'^register$', views.RegistrationForm.as_view(), name='registration'),
                       url(r'^my_account/$', views.UserAccount.as_view(), name='account_details'),
)

urlpatterns += patterns('django.contrib.auth.views',
                        url(r'^login/$', 'login', {
                            'template_name': 'registration/login.html',
                        }, name='login'))
