from django.conf.urls import patterns, include, url
from tastypie.api import Api
from django_app.api import TodoResource, TagResource
from django.contrib import admin
admin.autodiscover()

todo_resource = TodoResource()

urlpatterns = patterns('',
    url(r'^index/$', 'django_app.views.index'),
    url(r'^api/', include(todo_resource.urls)),
    # Examples:
    # url(r'^$', 'GetItDone.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
