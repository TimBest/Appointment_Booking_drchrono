from django.conf.urls import patterns, url


#TODO: add password reset form
urlpatterns = patterns('accounts.views',
    url(r'^logout/$', 'logout', name='logout'),
    url(r'^signup/$', 'signup', name='signup'),
    url(r'^signin/$', 'login', name='login'),
)
