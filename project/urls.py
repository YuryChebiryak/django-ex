from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from django.conf.urls.static import static
#import settings

urlpatterns = patterns('',
    #url(r'^admin/', include(admin.site.urls)),
    url(r'view/(?P<id>\d*)/(?P<pack>\d*)/(?P<pick>\d*)', \
            'project.view.show'), \
    url(r'view/(?P<id>\d*)', 'project.view.show'),
    url(r'recent', 'project.recent.show'),
    url(r'^$', 'project.mainpage.show'),
    url(r'main', 'project.mainpage.show'),
    url(r'submit', 'project.submit.draft'),
    url(r'donate', 'project.donate.show'),
    url(r'updateIndex', 'project.updater.updateindex'),
)
