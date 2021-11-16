from rest_framework import serializers
from .models import *

class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tags
        fields = ('__all__')

class ModelBlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ModelBlog
        fields = ('__all__')

