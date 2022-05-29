from django.contrib import admin
from .models import *
from django.utils.html import format_html
from django.contrib.auth.models import Permission


class FeedPostAdmin(admin. ModelAdmin):
    list_display = ("title", "author", "publisheddate", "updateddate")
    list_filter = ("title", "author", "publisheddate", "updateddate")
    search_fields = ("title", "author", "publisheddate", "updateddate")


admin.site.register(FeedPost, FeedPostAdmin)


class BannerAdmin(admin. ModelAdmin):
    list_display = ("title", "BannerImage")


admin.site.register(Banner, BannerAdmin)
# Register your models here.
