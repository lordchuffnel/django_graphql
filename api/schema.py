import graphene
from graphene_django import DjangoObjectType

from api.models import Movie, Director


class MovieType(DjangoObjectType):
  class Meta:
    model = Movie

  movie_age = graphene.String()

  def resolve_movie_age(self, info):
    return "old movie" if self.year < 2000 else "new movie"


class DirectorType(DjangoObjectType):
  class Meta:
    model = Director

class Query(graphene.ObjectType):
  all_movies = graphene.List(MovieType)
  movie = graphene.Field(MovieType, id=graphene.Int(), jtitle=graphene.String())
  
  all_directors = graphene.List(DirectorType)

  def resolve_all_movies(self, info, **kwargs):
    return Movie.objects.all()

  def resolve_all_directors(self, info, **kwargs):
    return Director.objects.all()

  def resolve_movie(self, info, **kwargs):
    id = kwargs.get('id')
    title = kwargs.get('title')

    if id is not None:
      return Movie.objects.get(pk=id)

    if title is not None:
      return Movie.objects.get(title=title)

    return None

class MovieCreateMutation(graphene.Mutation):
  class Arguments:
    title = graphene.String(required=True)
    year = graphene.Int(required=True)

  movie = graphene.Field(MovieType)

  def mutate(self, info, title, year):
    movie = Movie.objects.create(title=title, year=year)

    return MovieCreateMutation(movie=movie)

class Mutation:
  create_move = MovieCreateMutation.Field()