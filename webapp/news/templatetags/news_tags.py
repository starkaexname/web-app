from news.models import Category
from django import template

register = template.Library()


@register.inclusion_tag('news/list_categories.html')
def show_categories():
    categories = Category.objects.all()
    return {'categories': categories}

