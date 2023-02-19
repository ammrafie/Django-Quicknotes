from django.shortcuts import render
from django.http import Http404
from django.http.response import HttpResponseRedirect

from .models import Notes
from .forms import NotesForm
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


class NotesDeleteView(DeleteView):
    model = Notes
    context_object_name = "note"
    success_url = '/quicknotes/notes'
    template_name = "notes/notes_delete.html"


class NotesUpdateView(UpdateView):
    model = Notes
    form_class = NotesForm
    success_url = '/quicknotes/notes'
    template_name = "notes/notes_form.html"


class NotesCreateView(CreateView):
    model = Notes
    form_class = NotesForm
    success_url = '/quicknotes/notes'
    template_name = "notes/notes_form.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    login_url = "/login"
    context_object_name = "notes"
    template_name = "notes/notes_list.html"

    def get_queryset(self):
        return self.request.user.notes.all()


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"
    template_name = "notes/note.html"


# def noteslist_view(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/note_list.html', {'notes': all_notes})

# def note_view(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404('Note does not exist!')
#     return render(request, 'notes/note.html', {'note':note})
