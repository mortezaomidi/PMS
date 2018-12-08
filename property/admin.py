from django.contrib.gis import admin as geoadmin
from .models import Province, County, Property, PostalCode, EndUser
from leaflet.admin import LeafletGeoAdmin


@geoadmin.register(Property)
class PropertyAdmin(geoadmin.BingGeoAdmin):
    list_display = ([f.name for f in Property._meta.get_fields() if f.name != 'geom'])
    # list_filter = ('price')
    search_fields = ('contract_code', 'postal_code')
    date_hierarchy = 'recorded_date'


geoadmin.site.register(Province, geoadmin.BingGeoAdmin)
geoadmin.site.register(County, geoadmin.BingGeoAdmin)
geoadmin.site.register(PostalCode, geoadmin.BingGeoAdmin)
geoadmin.site.register(EndUser, geoadmin.BingGeoAdmin)


geoadmin.site.site_header =  "سامانه اطلاعات مکانی املاک و مستغلات"
geoadmin.site.index_title = 'داشبورد مدیریتی'
geoadmin.site.site_title = "سامانه اطلاعات مکانی املاک و مستغلات"
