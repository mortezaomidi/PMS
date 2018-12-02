from django.utils.encoding import python_2_unicode_compatible
from django.contrib.gis.db import models as geomodel


# SRID ==> Spatial refrence # IDEA
SRID = 4326

@python_2_unicode_compatible
class Province(geomodel.Model):
    province_id = geomodel.IntegerField("Province ID", primary_key=True)
    name = geomodel.CharField(max_length=50)
    # GIS field-specific: a geometry field (MultiPolygonField)
    geom = geomodel.MultiPolygonField(srid=SRID)

    # string representation of the object.
    def __str__(self):              # __unicode__ on Python 2
        return self.name

    class Meta:
        verbose_name = 'استان'
        verbose_name_plural = 'استان ها'

@python_2_unicode_compatible
class County(geomodel.Model):
    county_id = geomodel.IntegerField("County ID", primary_key=True)
    name = geomodel.CharField(max_length=50)
    # GIS field-specific: a geometry field (MultiPolygonField)
    geom = geomodel.MultiPolygonField(srid=SRID)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'َشهرستان'
        verbose_name_plural = 'شهرستان ها'


@python_2_unicode_compatible
class Property(geomodel.Model):
    """Base class for handelling property objects."""

    # contract type ==> CT
    CT_1 = 1
    CT_2 = 2
    CT = (
        (CT_1, 'مبایعه نامه'),
        (CT_2, 'وکالت'),
    )

    # property type ==> PT
    PT_1 = 1
    PT_2 = 2
    PT = (
        (PT_1, 'آپارتمان'),
        (PT_2, 'زمین'),
    )

    # land-use type ==> LUT
    RESIDENTIAL = 1
    COMMERCIAL = 2
    LUT = (
        (RESIDENTIAL, 'مسکونی'),
        (COMMERCIAL, 'تجاری'),
    )

    # structure type ==> ST
    NO_STRUCTURE = 0
    CONCRET = 1
    MENTAL = 2
    CONCRET_MENTAL = 3
    BRICK = 4
    ST = (
        (NO_STRUCTURE, 'بدون اسکلت'),
        (CONCRET, 'بتونی'),
        (MENTAL, 'فلزی'),
        (CONCRET_MENTAL, 'بتونی و فلزی'),
        (BRICK, 'بتونی و فلزی'),
        (BRICK, 'آجر یا بلوک سیمانی'),
    )

    contract_code = geomodel.CharField("Contract Code", max_length=8)
    contract_type = geomodel.PositiveSmallIntegerField("Contract Code",
        choices=CT)
    province = geomodel.ForeignKey(Province, on_delete=geomodel.CASCADE)
    county = geomodel.ForeignKey(County, on_delete=geomodel.CASCADE)
    property_type = geomodel.PositiveSmallIntegerField("Contract Code",
        choices=PT)
    region = geomodel.PositiveSmallIntegerField(blank=True, null=True)
    landuse = geomodel.PositiveSmallIntegerField(choices=PT)
    area = geomodel.FloatField()
    percentage = geomodel.FloatField()
    price = geomodel.FloatField()
    price_per = geomodel.FloatField("Price per square meter")
    building_age = geomodel.SmallIntegerField("Building Age")
    structure_type = geomodel.SmallIntegerField("Structure Type",
        choices=ST)
    recorded_date = geomodel.DateField() # auto_now=False, auto_now_add=False
    postal_code = geomodel.CharField("The first six digits of the zip code",
        max_length=6)

    # GIS field-specific: a geometry field (MultiPolygonField)
    geom = geomodel.MultiPolygonField(srid=SRID, blank=True)

    def __str__(self):
        return "({}, {}, {})".format(self.contract_code, self.price, self.postal_code)

    class Meta:
        verbose_name = 'ملک'
        verbose_name_plural = 'املاک'
