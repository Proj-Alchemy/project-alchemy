import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pass


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Vendor(BaseModel):
    pass


class TemplateFragment(BaseModel):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    group = models.CharField(max_length=10, default="", blank=True, null=True)
    template_text = models.TextField(default="", blank=True, null=True)


class DeviceUser(BaseModel):
    password = models.CharField(max_length=100)
    public_key = models.TextField()


class ManagementAddress(BaseModel):
    ip_address = models.GenericIPAddressField()


class Device(BaseModel):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    snmp_community = models.CharField(max_length=20)
    loopbackv4 = models.GenericIPAddressField(null=True, blank=True)
    loopbackv6 = models.GenericIPAddressField(null=True, blank=True)


class DeviceLink(BaseModel):
    device_a = models.ForeignKey(
        Device, on_delete=models.CASCADE, related_name="device_a"
    )
    port_a = models.CharField(max_length=100)
    device_b = models.ForeignKey(
        Device, on_delete=models.CASCADE, related_name="device_b"
    )
    port_b = models.CharField(max_length=100)
    ipv4_a = models.GenericIPAddressField()
    ipv6_a = models.GenericIPAddressField()
    ipv4_b = models.GenericIPAddressField()
    ipv6_b = models.GenericIPAddressField()
    ospf = models.BooleanField()
    mpls = models.BooleanField()
