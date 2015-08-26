from django.conf.urls import patterns, url


urlpatterns = patterns('appointments.views',
    url(r'^appointment/(?P<practice_id>\d+)/$', 'appointment_form', name='appointment_form'),
    url(r'^appointment/created/(?P<practice_id>\d+)/$', 'appointment_created', name='appointment_created'),

)
