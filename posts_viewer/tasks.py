from celery import Celery
from requests import get

from posts_viewer.serializers import PostsSerializer

app = Celery()

@app.task
def get_news(news_section):
    url = ('https://newsapi.org/v2/top-headlines?'
           'category={}&'
           'apiKey=71ff2393f666432cac9d3c7ce0b0762f'.format(news_section)
           )
    news = get(url).json().get('articles')
    if news:
        ser = PostsSerializer(data=news, many=True)
        if ser.is_valid():
            ser.save()
