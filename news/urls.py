from django.urls import path

from .views import news_list, news_detail
urlpatterns = [
    path('', news_list, name='news'),
    path('<int:news_id>/', news_detail, name='news_detail'),  # detay sayfası için
]
