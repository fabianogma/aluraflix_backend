from rest_framework import viewsets, generics, status
from aluraflix.models import Video
from aluraflix.serializer import DetalheDeVideoSerializer, VideoSerializer
from rest_framework.response import Response
from django.http import Http404

class VideosViewSet(viewsets.ModelViewSet):
    """Exibindo os Videos!"""
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    def destroy(self, request, *args, **kwargs):
        """Excluindo video"""
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except Http404:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"detail": "HTTP_404_NOT_FOUND"})
        return Response(status=status.HTTP_200_OK, data={"detail": "HTTP_200_OK"})

class DetalheDosVideos(generics.ListAPIView):
    """Detalhe de cada video"""
    def get_queryset(self):
        queryset = Video.objects.filter(video_id = self.kwargs['pk'])
        return queryset
    serializer_class = DetalheDeVideoSerializer