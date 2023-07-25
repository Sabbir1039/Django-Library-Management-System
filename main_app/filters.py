import django_filters
from .models import Author, Book


class AuthorFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        field_name='name', lookup_expr='icontains')
    country = django_filters.CharFilter(
        field_name='country', lookup_expr='icontains')

    class Meta:
        model = Author
        fields = ['name', 'country']


class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        field_name='title', lookup_expr='icontains')
    language = django_filters.CharFilter(
        field_name='language', lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ['title', 'language']
