from django.contrib import admin
from .models import Brand, PhoneModel
# Register your models here.

@admin.register(PhoneModel)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ["phone_model", "phone_brand"]
    
    class Media:
        js = ["js/custom-user.js", ]
    
    
@admin.register(Brand)
class BrandAmin(admin.ModelAdmin):
    pass



