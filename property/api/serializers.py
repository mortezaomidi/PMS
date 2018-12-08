from rest_framework.serializers import ModelSerializer
from property.models import Property

class PropertyCreateSerilizer(ModelSerializer):
    class Meta:
        model = Property
        exclude = ('user',)


class PropertyListSerilizer(ModelSerializer):
    class Meta:
        model = Property
        fields = ('contract_code', 'price', 'geom', )


class PropertyDetailSerilizer(ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'


class PropertyDeleteSerilizer(ModelSerializer):
    class Meta:
        model = Property
        exclude = ('user',)


class PropertyUpdateSerilizer(ModelSerializer):
    class Meta:
        model = Property
        exclude = ('user',)

class PropertymanageSerilizer(ModelSerializer):
    class Meta:
        model = Property
        exclude = ('user',)
