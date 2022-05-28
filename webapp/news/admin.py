from django.contrib import admin

# Register your models here.

from .models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'update_at', 'is_published', 'category')
    list_display_links = ('title', )
    search_fields = ('title', 'content')
    list_editable = ('category', )
    list_filter = ('category', 'is_published')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title', )


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)