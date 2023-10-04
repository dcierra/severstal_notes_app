from django.db import models
import uuid


class Note(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название заметки')
    description = models.TextField(blank=True, null=True, verbose_name='Описание заметки')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)

    class Meta:
        ordering = ['-created']
