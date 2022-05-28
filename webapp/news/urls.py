from django.urls import path
from .views import *

urlpatterns = [
    path('', NewsList.as_view(), name='homepage'),
    path('category/<int:category_id>/', CategoryNews.as_view(), name='cat'),
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),
    path('news/add_news/', CreateNews.as_view(), name='add_news')
    ]
