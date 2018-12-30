from rest_framework_mongoengine import routers as mongorouters

from posts_viewer.views import PostsViewSet

merouter = mongorouters.DefaultRouter()
merouter.register(r'posts', PostsViewSet)

urlpatterns = [
]

urlpatterns += merouter.urls
