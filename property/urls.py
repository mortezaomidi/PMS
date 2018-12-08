from django.conf.urls import url
from djgeojson.views import GeoJSONLayerView
# from djgeojson.views import TiledGeoJSONLayerView
from . import views
from . import models


urlpatterns = [
    url(r'^home/', views.home, name="home"),
    url(r'^detail/(?P<pk>[0-9]+)$',
        views.PropertyDetailView.as_view(), name='property-detail'),
    url(r'^list',
        views.PropertyListView.as_view(), name='property-list'),
    url(r'^new', views.NewPropertyView.as_view(), name='new-property'),
    url(r'^form',
        views.PropertyFormView.as_view(), name='property-form'),
    url(r'^data/province.geojson$', GeoJSONLayerView.as_view(
        model=models.Province, properties=('name',)), name='data_province'),
    url(r'^data/county.geojson$', GeoJSONLayerView.as_view(
        model=models.County, properties=('name',)), name='data_county'),
    url(r'^data/postalcode.geojson$', GeoJSONLayerView.as_view(
        model=models.PostalCode, properties=('postalcode',)), name='data_postalcode'),
    url(r'^data/property.geojson$', GeoJSONLayerView.as_view(
        model=models.Property, properties=('contract_code',)), name='data_property'),
    #url(r'^data/(\d+)/(\d+)/(\d+).geojson$',
        #TiledGeoJSONLayerView.as_view(model=models.Property, properties=('postalcode',)), name='data'),


]
