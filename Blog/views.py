from django.shortcuts import render
from .models import *
from .Serializers import *
from rest_framework import viewsets


class TagView(viewsets.ModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagSerializer

class ModelBlogView(viewsets.ModelViewSet):
    queryset = ModelBlog.objects.all()
    serializer_class = ModelBlogSerializer


