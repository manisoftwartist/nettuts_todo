from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nettuts_todo.views.home', name='home'),
    # url(r'^nettuts_todo/', include('nettuts_todo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    (r'^$', 'coreapp.views.mb_index'), #Our index page, it maps to / . Once the page is called it will look in /todo/coreapp/views.py for a function called mb_index
)
