from rest_framework import routers
from rest_framework import serializers
from rest_framework import viewsets

from main.models import Device
from main.models import DeviceLink
from main.models import TemplateFragment
from main.models import Vendor


class BaseViewSet(viewsets.ModelViewSet):
    http_method_names = ["get", "post", "put", "delete"]


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = "__all__"


class DeviceViewSet(BaseViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = "__all__"


class VendorViewSet(BaseViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class TemplateFragmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemplateFragment
        fields = "__all__"


class TemplateFragmentViewSet(BaseViewSet):
    queryset = TemplateFragment.objects.all()
    serializer_class = TemplateFragmentSerializer


class DeviceLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceLink
        fields = "__all__"


class DeviceLinkViewSet(BaseViewSet):
    queryset = DeviceLink.objects.all()
    serializer_class = DeviceLinkSerializer


router = routers.DefaultRouter()
router.register(r"vendor", VendorViewSet)
router.register(r"template", TemplateFragmentViewSet)
router.register(r"device", DeviceViewSet)
router.register(r"devicelink", DeviceLinkViewSet)
