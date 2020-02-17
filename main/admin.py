from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Device
from .models import DeviceLink
from .models import DeviceUser
from .models import ManagementAddress
from .models import User
from .models import Vendor


class BaseAdmin(admin.ModelAdmin):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields]
        super(BaseAdmin, self).__init__(model, admin_site)


class DeviceAdmin(BaseAdmin):
    pass


class VendorAdmin(BaseAdmin):
    pass


class DeviceLinkAdmin(BaseAdmin):
    pass


class DeviceUserAdmin(BaseAdmin):
    pass


class ManagementAddressAdmin(BaseAdmin):
    pass


admin.site.register(User, UserAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(DeviceLink, DeviceLinkAdmin)
admin.site.register(DeviceUser, DeviceUserAdmin)
admin.site.register(ManagementAddress, ManagementAddressAdmin)
