from django.contrib import admin
from .models import ShortUrl


class ShortUrAdmin(admin.ModelAdmin):
    list_display = ('pk', 'url', 'author')
    list_display_links = ('url', 'author')


admin.site.register(ShortUrl, ShortUrAdmin)
