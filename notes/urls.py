# notes/urls.py

from django.urls import path
from .views import NoteListView, NoteCreateView, NoteUpdateView, NoteDeleteView

urlpatterns = [
    path('', NoteListView.as_view(), name='note-list'),
    path('new/', NoteCreateView.as_view(), name='note-create'),
    path('<int:pk>/edit/', NoteUpdateView.as_view(), name='note-update'),
    path('<int:pk>/delete/', NoteDeleteView.as_view(), name='note-delete'),
]
