from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'twitter_db.views.home', name='home'),
    url(r'^status/$', 'twitter_db.apps.twitter_stream.views.status_view', name='status'),
    url(r'^admin/', include(admin.site.urls)),
)
