#todolist_app\urls.py
from django.urls import path
from todolist_app import views as todolist_views

urlpatterns = [
    path('', todolist_views.todolist, name='todolist'),
    path('delete/<task_id>', todolist_views.delete_task, name='delete_task'),
    path('edit/<task_id>', todolist_views.edit_task, name='edit_task'),
    path('complete/<task_id>', todolist_views.complete_task, name='complete_task'),
    path('pending/<task_id>', todolist_views.pending_task, name='pending_task'),
    path('contact', todolist_views.contact, name='contact'),
    path('about-us', todolist_views.about, name='about'),
]
