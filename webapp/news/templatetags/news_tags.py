from news.models import Category
from django import template
from django.core.cache import cache

register = template.Library()


@register.inclusion_tag('news/list_categories.html')
def show_categories():
    categories = cache.get_or_set('categories', Category.objects.all(), 15)
    # categories = Category.objects.all()
    return {'categories': categories}
