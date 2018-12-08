from django.conf.urls import url
from .import views


urlpatterns = [
    url(r'^$', views.PropertyListApiView.as_view(), name="property-list"),
    url(r'^create/(?P<id>[0-9]+)$', views.PropertyCreateApiView.as_view(),
     name="property-create"),
    url(r'^detail/(?P<contract_code>[0-9]+)$', views.PropertyDetailApiView.as_view(),
     name="property-detail"),
    url(r'^delete/(?P<contract_code>[0-9]+)$', views.PropertyDeleteApiView.as_view(),
     name="property-delete"),
    url(r'^update/(?P<contract_code>[0-9]+)$', views.PropertyUpdateApiView.as_view(),
     name="property-update"),
    url(r'^manage/(?P<contract_code>[0-9]+)$', views.PropertyManageApiView.as_view(),
     name="property-manage"),

]
