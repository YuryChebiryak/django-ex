from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from django.conf.urls.static import static
#import settings

urlpatterns = patterns('',
    #url(r'^admin/', include(admin.site.urls)),
    #url(r'view/(?P<id>\d*)/(?P<pack>\d*)/(?P<pick>\d*)', \
        'view.show'), \
    #url(r'view/(?P<id>\d*)', 'view.show'),
    #url(r'recent', 'recent.show'),
    url(r'^$', 'mainpage.show'),
    url(r'main', 'mainpage.show'),
    #url(r'submit', 'submit.draft'),
    #url(r'donate', 'donate.show'),
    #url(r'updateIndex', 'updater.updateindex'),
)
