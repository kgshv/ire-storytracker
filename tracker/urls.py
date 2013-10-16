from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'tracker.list.views.index', name='index'),
    url(r'^impacts/$', 'tracker.list.views.impact_list', name='impact_list'),
    url(r'^impacts/(?P<slug>.*)/$', 'tracker.list.views.impact_detail', name='impact_detail'),
    url(r'^articles/$', 'tracker.list.views.article_index', name='article_index'),
    url(r'^articles/(?P<slug>.*)/$', 'tracker.list.views.article_detail', name='article_detail'),
    url(r'^training/$', 'tracker.list.views.training_index', name='training_index'),
    url(r'^training/(?P<slug>.*)/$', 'tracker.list.views.training_detail', name='training_detail'),
    url(r'^share/$', 'tracker.list.views.contact', name='share'),
    url(r'^thanks/$', 'tracker.list.views.thanks', name='thanks'),


	
	(r'^mapjson/', 'tracker.list.views.map_api'),
    # url(r'^tracker/', include('tracker.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

)
