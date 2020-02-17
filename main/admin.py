from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Device
from .models import DeviceLink
from .models import DeviceUser
from .models import ManagementAddress
from .models import TemplateFragment
from .models import User
from .models import Vendor


class BaseAdmin(admin.ModelAdmin):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields]
        super(BaseAdmin, self).__init__(model, admin_site)


admin.site.register(User, UserAdmin)
admin.site.register(Vendor)
admin.site.register(Device)
admin.site.register(DeviceLink)
admin.site.register(DeviceUser)
admin.site.register(ManagementAddress)
admin.site.register(TemplateFragment)
