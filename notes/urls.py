from django.urls import path
from . import views
from . import api_views

urlpatterns = [
    path('api/v1/notes/', api_views.NotesListAPIView.as_view()),

    path('notes', views.NotesListView.as_view(), name="notes.list"),
    path('note/<int:pk>', views.NotesDetailView.as_view(), name="notes.detail"),
    path('note/new', views.NotesCreateView.as_view(), name="notes.new"),
    path('note/<int:pk>/edit', views.NotesUpdateView.as_view(), name="notes.update"),
    path('note/<int:pk>/delete', views.NotesDeleteView.as_view(), name="notes.delete")
]
