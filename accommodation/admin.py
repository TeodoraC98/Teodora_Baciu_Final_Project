from django.contrib import admin
from .models import Room,RoomType,Package,BenefitsPackage
admin.site.register(Room)
admin.site.register(RoomType)
admin.site.register(Package)
admin.site.register(BenefitsPackage)

