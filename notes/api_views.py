from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend

from .models import Notes
from .serializers import NotesSerializer


class NotesPagination(LimitOffsetPagination):
    default_limit = 3
    max_limit = 10


class NotesListAPIView(ListAPIView):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ['id']
    search_fields = ('title', 'text')
    pagination_class = NotesPagination

    def get_queryset(self):
        post_about_django = self.request.query_params.get(
            'is_about_django', None)
        if post_about_django is None:
            return super().get_queryset()
        queryset = Notes.objects.all()
        if post_about_django.lower() == 'true':
            return queryset.filter(title__icontains="django").filter(title__icontains="Django")
        elif post_about_django.lower() == 'false':
            return queryset.exclude(title__icontains="django").exclude(title__icontains="Django")

#
#
# API View automatically renders serialized data into JSON format
