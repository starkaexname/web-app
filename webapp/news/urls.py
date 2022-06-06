from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page


urlpatterns = [
    # path('', cache_page(30)(NewsList.as_view()), name='homepage'),
    path('', NewsList.as_view(), name='homepage'),
    path('category/<int:category_id>/', CategoryNews.as_view(), name='cat'),
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),
    path('news/add_news/', CreateNews.as_view(), name='add_news'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout', user_logout, name='logout'),
    path('AdMailto/', admailto, name='AdMailto')
    ]
