from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import AbstractUser
from django.contrib.gis.db import models as geomodel
from django.contrib.gis.gdal import SpatialReference, CoordTransform
from django.contrib.gis.geos import GEOSGeometry, Point
import random


# SRID ==> Spatial refrence # IDEA
SRID = 4326

class EndUser(AbstractUser):
    geom = geomodel.MultiPolygonField(srid=SRID, verbose_name='موقعیت بنگاه', blank=True, null=True)
    is_citizen = geomodel.BooleanField(default=True, verbose_name="مشاور املاک عادی")
    is_expert = geomodel.BooleanField(default=False, verbose_name='مشاور املاک ویژه')
    is_admin = geomodel.BooleanField(default=False, verbose_name='شرکت مادر تخصصی')


@python_2_unicode_compatible
class Province(geomodel.Model):
    province_id = geomodel.IntegerField('کد استان', primary_key=True)
    name = geomodel.CharField('نام', max_length=50)
    # GIS field-specific: a geometry field (MultiPolygonField)
    geom = geomodel.MultiPolygonField('محدوده جغرافیایی', srid=SRID)

    # string representation of the object.
    def __str__(self):              # __unicode__ on Python 2
        return self.name

    class Meta:
        verbose_name = 'استان'
        verbose_name_plural = 'استان ها'


@python_2_unicode_compatible
class County(geomodel.Model):
    county_id = geomodel.IntegerField('کد شهرستان', primary_key=True)
    province = geomodel.ForeignKey(Province, on_delete=geomodel.CASCADE, verbose_name='استان')
    name = geomodel.CharField('نام شهرستان', max_length=50)
    # GIS field-specific: a geometry field (MultiPolygonField)
    geom = geomodel.MultiPolygonField('محدوده جغرافیایی', srid=SRID)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'َشهرستان'
        verbose_name_plural = 'شهرستان ها'


@python_2_unicode_compatible
class PostalCode(geomodel.Model):
    id = geomodel.AutoField(primary_key=True)
    postalcode = geomodel.CharField(max_length=5, verbose_name='کدپستی', default="")
    geom = geomodel.MultiPolygonField('محدوده جغرافیایی', srid=32639, blank=True, null=True)

    def __str__(self):
        return "واحد مکانی پستی: " + self.postalcode

    class Meta:
        verbose_name = 'کد پستی'
        verbose_name_plural = 'کدهای پستی'


@python_2_unicode_compatible
class Property(geomodel.Model):
    '''Base class for handelling property objects.'''

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
    WOOD = 5
    ST = (
        (NO_STRUCTURE, 'بدون اسکلت'),
        (CONCRET, 'بتونی'),
        (MENTAL, 'فلزی'),
        (CONCRET_MENTAL, 'بتونی و فلزی'),
        (BRICK, 'بتونی و فلزی'),
        (BRICK, 'آجر یا بلوک سیمانی'),
        (WOOD, 'چوب'),
    )

    @classmethod
    def get_random_point(cls, geom):
        # Return random point in  bounds of a postalcode.
        desired_srid = SpatialReference(SRID)
        source_srid = SpatialReference(geom.srid)
        trans = CoordTransform(source_srid, desired_srid)
        geom.transform(trans)
        bounds = geom.extent
        min_x, min_y, max_x, max_y = bounds
        # Return a random floating point number N such that ...
        #... a <= N <= b for a <= b and b <= N <= a for b < a.
        x = random.uniform(min_x, max_x)
        y = random.uniform(min_y, max_y)
        pnt = Point(x,y, srid=SRID)

        return GEOSGeometry(pnt)

    user = geomodel.ForeignKey(EndUser, on_delete=geomodel.CASCADE,
        verbose_name='مشاور')
    contract_code = geomodel.CharField('کد قرارداد', max_length=8)
    contract_type = geomodel.PositiveSmallIntegerField('نوع قرارداد',
        choices=CT)
    province = geomodel.ForeignKey( Province, on_delete=geomodel.CASCADE,
        verbose_name='استان')
    county = geomodel.ForeignKey(County, on_delete=geomodel.CASCADE,
        verbose_name='شهرستان')
    property_type = geomodel.PositiveSmallIntegerField('نوع ملک',
        choices=PT)
    region = geomodel.PositiveSmallIntegerField('منطقه', blank=True, null=True)
    landuse = geomodel.PositiveSmallIntegerField('کاربری', choices=LUT)
    area = geomodel.FloatField('مساحت')
    percentage = geomodel.FloatField('درصد')
    price = geomodel.FloatField('قیمت')
    price_per = geomodel.FloatField('قیمت هر متر مربع')
    building_age = geomodel.SmallIntegerField('قدمت بنا')
    structure_type = geomodel.SmallIntegerField('نوع سازه',
        choices=ST)
    recorded_date = geomodel.DateField('تاریخ ثبت قرارداد') # auto_now=False, auto_now_add=False
    postal_code = geomodel.CharField('کد پستی', max_length=5) #unique=True

    # GIS field-specific: a geometry field (MultiPolygonField)
    geom = geomodel.PointField('موقعیت جغرافیایی', srid=SRID, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('property-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '({}, {}, {})'.format(self.contract_code, self.price, self.postal_code)

    class Meta:
        verbose_name = 'ملک'
        verbose_name_plural = 'املاک'
        ordering = ['-price']

    def save(self, *args, **kwargs):
        if not self.geom:
            try:
                postalcode_geom = PostalCode.objects.get(postalcode=self.postal_code)
                self.geom = self.get_random_point(postalcode_geom.geom)
                super(Property, self).save(*args, **kwargs)
                print('random point added to Property.')
            except Exception as e:
                print(e)
                self.geom = Point(0,0)
                super(Property, self).save(*args, **kwargs)
