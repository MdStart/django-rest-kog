from django.conf.urls import patterns, include, url
from rest_framework import routers 
from rest_demo.demo import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

router = routers.SimpleRouter()
router.register(r'posts', views.PostViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rest_demo.views.home', name='home'),
    # url(r'^rest_demo/', include('rest_demo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'api-docs/', include('rest_framework_swagger.urls')),
    url(r'api-docs-plain/', include('rest_framework_docs.urls')),
)
