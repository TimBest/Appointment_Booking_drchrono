from django.conf.urls import patterns, url


#TODO: add password reset form
urlpatterns = patterns('accounts.views',
    url(r'^appointment/(?P<practice_id>\d+)/$', 'appointment_form', name='appointment_form'),
    url(r'^logout/$', 'logout', name='logout'),
    url(r'^signup/$', 'signup', name='signup'),
    url(r'^signin/$', 'login', name='login'),
)
