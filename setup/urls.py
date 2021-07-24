from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from aluraflix.views import DetalheDosVideos, VideosViewSet

router = routers.DefaultRouter()
router.register('videos', VideosViewSet, basename = 'Videos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('videos/<int:pk>/', DetalheDosVideos.as_view())
]