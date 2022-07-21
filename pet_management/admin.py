from django.contrib import admin

from .models import Pet


class PetAdmin(admin.ModelAdmin):
    pass


admin.site.register(Pet, PetAdmin)
