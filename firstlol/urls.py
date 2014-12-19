from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'firstlol.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^lol/$', 'lol.views.lol_search'),
    url(r'^search/$', 'lol.views.search'),
    url(r'^$', 'lol.views.example1'),
    url(r'^about/$', 'lol.views.about'),
    url(r'^contact/$', 'lol.views.contact'),
)
