from django.conf.urls import patterns, url


urlpatterns = patterns('accounts.views',
    url(r'^appointment/(?P<practice_id>\d+)$', 'appointment_form', name='appointment_form'),
    url(r'^logout/$', 'logout', name='logout'),
)
