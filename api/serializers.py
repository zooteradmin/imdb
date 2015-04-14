from django.forms import widgets
from rest_framework import serializers
from api.models import Movie, Director, Genre

class DirectorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Director
    fields = ('id', 'name')

class GenreSerializer(serializers.ModelSerializer):
  class Meta:
    model = Genre
    fields = ('id', 'name')


class MovieSerializer(serializers.ModelSerializer):
  genres = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
  director = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
  class Meta:
    model = Movie
    fields = ('id', 'name', 'imdb_score', 'popularity', 'director', 'genres')