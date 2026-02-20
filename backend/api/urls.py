from django.urls import path
from api.views import NoteListCreateApiview, NoteDeleteApiview

urlpatterns = [
    path('notes/', NoteListCreateApiview.as_view(), name="note-create-list"),
    path('notes/delete/<int:pk>/', NoteDeleteApiview.as_view(), name="note-destroy"),
]
