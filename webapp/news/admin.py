from django.contrib import admin
from django_ckeditor_5.widgets import CKEditor5Widget
from django.utils.safestring import mark_safe
from django import forms
from .models import News, Category


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(label="Текст", widget=CKEditor5Widget(config_name="extends"))

    class Meta:
        model = News
        fields = ['title', 'content', 'is_published', 'category']


class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = ('id', 'title', 'created_at', 'update_at', 'is_published', 'category', 'showphoto', 'views')
    list_display_links = ('title', )
    search_fields = ('title', 'content')
    list_editable = ('category', )
    list_filter = ('category', 'is_published')
    fields = ('title', 'content', 'photo', 'showphoto', 'created_at', 'update_at', 'is_published', 'category', 'views')
    readonly_fields = ('showphoto', 'created_at', 'update_at', 'views')
    save_on_top = True

    def showphoto(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75" height="60"')
        else:
            return 'Нет фото'
            # return mark_safe(f'<img src="https://picsum.photos/id/1018/300/200" width="75" alt=""')
    showphoto.short_description = 'фото'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title', )


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = "Кабинет администратора"
admin.site.site_header = "Кабинет администратора"
