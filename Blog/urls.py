from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from Blog import views

router = routers.DefaultRouter()
router.register(r'tags', views.TagView)
router.register(r'mb', views.ModelBlogView)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
