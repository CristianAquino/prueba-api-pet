from django.contrib import admin

from adoptions.models import Adoption, AdoptionDetail

# Register your models here.

class AdoptionAdmin(admin.ModelAdmin):
    pass
class AdoptionDetailAdmin(admin.ModelAdmin):
    pass

admin.site.register(Adoption, AdoptionAdmin)
admin.site.register(AdoptionDetail, AdoptionDetailAdmin)