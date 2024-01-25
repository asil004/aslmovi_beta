from django.http import HttpResponse
from django.shortcuts import render
from django_filters.views import FilterView
from home.filters import MovieFilter
from home.models import Movie
from django.views.generic import DetailView


class HomeView(FilterView):
    model = Movie
    queryset = Movie.objects.all()
    context_object_name = 'latest_movies'
    template_name = 'home/index.html'
    filterset_class = MovieFilter


class MovieDetailView(DetailView):
    model = Movie
    context_object_name = 'movies'
    template_name = 'home/moviesingle.html'
