from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='notes_home_page'),
    path('note_create', views.note_create, name='note_create'),
    path('note_update/<str:note_id>/', views.note_update, name='note_update'),
    path('note_delete/<str:note_id>/', views.note_delete, name='note_delete'),
]