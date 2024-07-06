from django.contrib import admin
from .models import Discounts, AirConditioner, MobilePhones, HouseholdAppliances,\
    Books, TV, Laptops

# Register your models here.
admin.site.register(Discounts)
admin.site.register(AirConditioner)
admin.site.register(MobilePhones)
admin.site.register(HouseholdAppliances)
admin.site.register(Books)
admin.site.register(TV)
admin.site.register(Laptops)