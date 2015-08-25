from django.conf import settings
from django.conf.urls import include, patterns, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.sitemaps.views import sitemap

from appointment_booking_drchrono.sitemap import StaticViewSitemap


sitemaps = {
    'static': StaticViewSitemap(),
}

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^autocomplete/', include('autocomplete_light.urls')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    url(r'^robots.txt$', include('robots.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
)

urlpatterns += patterns('accounts.views',
    url(r'^$', 'home', name='home'),
)

urlpatterns += patterns('',
    url(r'', include('accounts.urls')),
)

if settings.DEVELOPMENT:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()
