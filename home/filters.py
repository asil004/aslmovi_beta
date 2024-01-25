from django_filters import FilterSet, CharFilter
from .models import Movie
from django import forms


class MovieFilter(FilterSet):
    title = CharFilter(lookup_expr='icontains', label='Title', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Movie
        fields = ['title']


