from django.conf.urls import patterns, include, url
from todo import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import viewsets, routers

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
   # don't forget to disable on production
   url(r'^$', views.index),
   url(r'^admin/', include(admin.site.urls)),
   url(r'^view/', views.index),
   url(r'^register/$',views.RegistrationView.as_view()),

   url(r'^todos/$',views.TodosView.as_view()),
   url(r'^todo/(?P<todo_id>[0-9]*)$', views.TodosView.as_view()),

   url(r'^oauth2/',include('provider.oauth2.urls',namespace='oauth2')),
   url(r'^api-oauth/', include('rest_framework.urls',namespace='rest_framework'))
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)