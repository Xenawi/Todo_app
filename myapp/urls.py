from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name='home'),
    path("todo-list/", views.todo_list, name='todo_list'),
    path("add-todo/", views.add_todo, name='add_todo'),
    path("todo-update/<int:todo_id>/", views.todo_update, name='update_todo'),
    path("todo-delete/<int:todo_id>/", views.todo_delete, name='delete_todo'),
    path('done/<int:todo_id>/', views.toggle_done, name='toggle_done'),

]