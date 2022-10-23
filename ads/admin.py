from django.contrib import admin

from ads.models.ad import Ad
from ads.models.category import Category


class AdsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_published', 'image')
    list_display_links = ('id', 'name')
    search_fields = ('image', 'description')
    list_editable = ("is_published",)
    list_filter = ('is_published',)


admin.site.register(Ad, AdsAdmin)
admin.site.register(Category)
