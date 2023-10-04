from .models import Note
from django.forms import ModelForm


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = [
            'title',
            'description',
        ]

    def __init__(self, *args, **kwargs):
        super(NoteForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
