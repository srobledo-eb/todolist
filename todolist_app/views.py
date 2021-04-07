from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from .models import Todo, Priority
from django.urls import reverse_lazy


class CreateTodoView(CreateView):
    model = Todo
    fields = ['description', 'priority', 'done']
    success_url = reverse_lazy('todolist_app:todo_list')

    def is_valid(self, form):
        form.instance.assigned_user = self.request.user
        return super().is_valid(form)

class UpdateTodoView(UpdateView):
    model = Todo
    fields = ['description', 'priority', 'done']
    success_url = reverse_lazy('todolist_app:todo_list')

class UpdateUserView(UpdateView):
    model = Todo
    fields = ['assigned_user']
    success_url = reverse_lazy('todolist_app:todo_list')

class CreatePriorityView(CreateView):
    model = Priority
    fields = '__all__'
    success_url = reverse_lazy('todolist_app:todo_list')

class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy('todolist_app:todo_list')
    # success_url = reverse_lazy('Todo-list')

class TodoListView(ListView):
    model = Todo
