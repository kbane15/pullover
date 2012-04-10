from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'pullover.locater.views.home', name='home'), 
    url(r'^town/(?P<town_id>\d+)/$', 'pullover.locater.views.detail'),
    # url(r'^town/info/(?P<info_id>\d+)/$', 'pullover.information.views.info'),

    # url(r'^$', 'pullover.views.home', name='home'),
    # url(r'^pullover/', include('pullover.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
