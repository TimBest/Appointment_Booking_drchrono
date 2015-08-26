from django.conf.urls import patterns, url


#TODO: add password reset form
urlpatterns = patterns('accounts.views',
    url(r'^logout/$', 'logout', name='logout'),
    url(r'^signup/(?P<practice_id>\d+)/$', 'signup', name='signup'),
    url(r'^signin/$', 'login', name='login'),
    url(r'^my-practice/$', 'practice_profile', name='practice_profile'),
    url(r'^profile/$', 'patient_profile', name='patient_profile'),
)
