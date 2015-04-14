from django.forms import widgets
from rest_framework import serializers
from api.models import Movie, Director, Genre

class DirectorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Director
    fields = ('id', 'name')
    read_only_fields = ('id',)

class GenreSerializer(serializers.ModelSerializer):
  class Meta:
    model = Genre
    fields = ('id', 'name')
    read_only_fields = ('id',)


class MovieSerializer(serializers.ModelSerializer):
  director = DirectorSerializer()
  genres = GenreSerializer(many=True)
  class Meta:
    model = Movie
    fields = ('id', 'name', 'imdb_score', 'popularity', 'director', 'genres')
    read_only_fields = ('id',)
  def create(self, validated_data):
    director_data = validated_data.pop('director')
    genres_data = validated_data.pop('genres')
    d = Director.objects.create(name=director_data['name'])
    validated_data['director_id'] = d.pk
    movie = Movie.objects.create(**validated_data)
    for data in genres_data:
      g = Genre.objects.create(name=data['name'])
      movie.genres.add(g)
    return movie