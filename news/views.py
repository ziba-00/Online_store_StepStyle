from django.shortcuts import render

from news.models import News


def news_list(request):
    news = News.objects.order_by('-created_at')
    return render(request, 'news_list.html', context={'news': news})

def news_detail(request, news_id):
    new = News.objects.get(id=news_id)
    return render(request, 'news_detail.html', context={'new': new})
