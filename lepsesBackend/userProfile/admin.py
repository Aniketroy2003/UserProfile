from django.contrib import admin
from .models.models import Location,School,Standard,Profile,ProfileCategory
# Register your models here.


admin.site.register(School)
admin.site.register(Location)
admin.site.register(Standard)
admin.site.register(Profile)
admin.site.register(ProfileCategory)


