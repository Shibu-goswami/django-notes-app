# notes/views.py

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Note
from .forms import NoteForm
from django.contrib.auth.forms import UserCreationForm




class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'notes/note_list.html'
    context_object_name = 'notes'
    paginate_by = 10  

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user).order_by('-created_at')

class NoteCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('note-list')
    success_message = "Note created successfully."

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class NoteUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('note-list')
    success_message = "Note updated successfully."

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)


class NoteDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Note
    template_name = 'notes/note_confirm_delete.html'
    success_url = reverse_lazy('note-list')
    success_message = "Note deleted successfully."

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)
