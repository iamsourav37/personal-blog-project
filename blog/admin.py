from django.contrib import admin
from .models import Category, Post
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("image_tag", "title", "description", "created_date")
    list_display_links = ("image_tag", "title", "description", "created_date")
    search_fields = ("title", "description")

    list_per_page = 5


class PostAdmin(admin.ModelAdmin):
    list_display = ("image_tag", "title", "likes", "created_date")
    list_display_links = ("image_tag", "title", "likes", "created_date")
    list_per_page = 5
    search_fields = ("title", "content", "url",)
    list_filter = ("category", )







admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)

