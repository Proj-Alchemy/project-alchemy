from jinja2 import Template
from jinja2 import UndefinedError
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ViewSet

from main.models import Device
from main.models import DeviceLink
from main.models import DeviceUser
from main.models import ManagementAddress


class DeviceSerializer(ModelSerializer):
    class Meta:
        model = Device
        fields = "__all__"


class DeviceUserSerializer(ModelSerializer):
    class Meta:
        model = DeviceUser
        fields = "__all__"


class DeviceLinkSerializer(ModelSerializer):
    class Meta:
        model = DeviceLink
        fields = "__all__"


class ManagementAddressSerializer(ModelSerializer):
    class Meta:
        model = ManagementAddress
        fields = "__all__"


class DeviceConfigViewSet(ViewSet):
    """ Generates a configuration, for a given device ID """

    permission_classes = [IsAuthenticated]

    def retrieve(self, request, pk=None):
        queryset = Device.objects.all()
        device = get_object_or_404(queryset, pk=pk)
        serializer = DeviceSerializer(device)

        device_data = serializer.data

        device_data["users"] = [
            DeviceUserSerializer(user).data for user in DeviceUser.objects.all()
        ]
        device_data["managementaddress"] = [
            ManagementAddressSerializer(address).data
            for address in ManagementAddress.objects.all()
        ]

        interfaces = []
        pop_list = [
            "ipv4_a",
            "ipv6_a",
            "port_a",
            "ipv4_b",
            "ipv6_b",
            "port_b",
            "device_a",
            "device_b",
        ]

        for interface in device.device_a.all():
            data = DeviceLinkSerializer(interface).data
            data["ipv4"] = data["ipv4_a"]
            data["ipv6"] = data["ipv6_a"]
            data["port"] = data["port_a"]
            for p in pop_list:
                data.pop(p)
            interfaces.append(data)

        for interface in device.device_b.all():
            data = DeviceLinkSerializer(interface).data
            data["ipv4"] = data["ipv4_b"]
            data["ipv6"] = data["ipv6_b"]
            data["port"] = data["port_b"]
            for p in pop_list:
                data.pop(p)
            interfaces.append(data)

        device_data["interfaces"] = interfaces

        template_data = device.vendor.templatefragment_set.first()

        try:
            template = Template(template_data.template_text)
            device_config = template.render({"device": device_data})
        except UndefinedError as e:
            device_config = repr(e)

        return Response({"vars": device_data, "config": device_config})
