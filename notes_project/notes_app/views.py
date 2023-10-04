from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from . import models


def home_page(request):
    notes = models.Note.objects.all()

    context = {'notes': notes}

    return render(request, 'notes_app/notes_home_page.html', context)


def note_create(request):
    form = forms.NoteForm

    if request.method == 'POST':
        form = forms.NoteForm(request.POST)

        if form.is_valid():
            note = form.save()
            return redirect('notes_home_page')

    context = {'form': form}
    return render(request, 'notes_app/note_form.html', context)


def note_update(request, note_id):
    note = get_object_or_404(models.Note, id=note_id)

    form = forms.NoteForm(instance=note)

    if request.method == 'POST':
        form = forms.NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes_home_page')

    context = {'form': form, 'note_id': note.id}
    return render(request, 'notes_app/note_form.html', context)


def note_delete(request, note_id):
    note = get_object_or_404(models.Note, id=note_id)

    if request.method == 'POST':
        note.delete()

    return redirect('notes_home_page')
