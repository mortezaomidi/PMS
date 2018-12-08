from rest_framework import generics
from django.core.exceptions import PermissionDenied
from property.models import Property
from .serializers import (
    PropertyCreateSerilizer,
    PropertyListSerilizer,
    PropertyDetailSerilizer,
    PropertyDeleteSerilizer,
    PropertyUpdateSerilizer,
    PropertymanageSerilizer,
    )
from property.models import EndUser


class PropertyCreateApiView(generics.CreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertyCreateSerilizer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PropertyListApiView(generics.ListAPIView):
    serializer_class = PropertyListSerilizer

    def get_queryset(self, *args, **kwargs):
        # just Tehran properties desired but...
        if self.request.user.is_superuser:
            queryset = Property.objects.all()
        else:
            queryset = Property.objects.filter(user=self.request.user)
        return queryset


class PropertyDetailApiView(generics.RetrieveAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertyDetailSerilizer
    lookup_field = "contract_code"


class PropertyDeleteApiView(generics.RetrieveDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertyDeleteSerilizer
    lookup_field = "contract_code"

    def perform_destroy(self, serilizer):
        admin = EndUser.objects.get(username='admin')
        if serilizer.user != self.request.user or serilizer.user != admin.is_superuser :
            raise PermissionError
        else:
            serilizer.delete()


class PropertyUpdateApiView(generics.RetrieveUpdateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertyUpdateSerilizer
    lookup_field = "contract_code"

    def perform_update(self, serilizer):
        serilizer.save(user=self.request.user)


class PropertyManageApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertymanageSerilizer
    lookup_field = "contract_code"
