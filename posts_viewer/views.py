from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_mongoengine import viewsets as mongoiewsets

from posts_viewer.models import Posts
from posts_viewer.serializers import PostsSerializer


class PostsViewSet(mongoiewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
