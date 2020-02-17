from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Device
from .models import User
from .models import Vendor


class DeviceAdmin(admin.ModelAdmin):
    pass


class VendorAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(Device, DeviceAdmin)
