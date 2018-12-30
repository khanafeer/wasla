from rest_framework_mongoengine import serializers

from posts_viewer.models import Posts


class PostsSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Posts
        fields = '__all__'

    def create(self, validated_data):
        try:
            obj = Posts.objects.get(content=validated_data.get('content'))
            return obj
        except Posts.DoesNotExist:
            return Posts.objects.create(**validated_data)
