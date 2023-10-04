from django.contrib import admin
from .models import Note


class NoteAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'created',
        'updated'
    ]

    list_display_links = [
        'id',
        'title'
    ]

    search_fields = [
        'title',
        'description'
    ]


admin.site.register(Note, NoteAdmin)
