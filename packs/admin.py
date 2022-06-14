from django.contrib import admin
from.models import Packs

class PacksAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating')


admin.site.register(Packs, PacksAdmin)