from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^$', 'twentyFour.views.home'),
    url(r'^twentyFour/', include('twentyFour.urls')),
)
