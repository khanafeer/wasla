from django.urls import include, path

urlpatterns = [
    path('', include('posts_viewer.urls'))
]
