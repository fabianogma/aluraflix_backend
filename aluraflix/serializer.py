from rest_framework import serializers
from aluraflix.models import Video

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'titulo', 'descricao', 'url']

class DetalheDeVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['titulo', 'descricao', 'url']