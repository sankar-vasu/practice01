from django.contrib import admin
from .models import tsc_stores,photo_upload,brand_names,Person_details
# Register your models here.
admin.site.register(tsc_stores)
admin.site.register(photo_upload)
admin.site.register(brand_names)
admin.site.register(Person_details)
