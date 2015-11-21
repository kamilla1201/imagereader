from imagereader import views
from imagereader.feed import urls
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'feed/', include(urls)),
    url(r'^$', views.home, name='home_page'),
    url(r'^', include('registration.backends.default.urls')),
    url(r'submit', include(urls)),
    url(r'^profile/add', views.add_url),
    url(r'^profile/filter', views.update_filter),
    url(r'^profile/clear', views.delete_images),
    url(r'^profile/delete', views.delete_url),
    url(r'^profile/view', include(urls)),
    url(r'^profile/', views.profile, name='user_profile'), 
    url(r'^error/', views.error), 

)
