from django.contrib import admin
from django.urls import path
from todolist_app.views import CreateTodoView
from todolist_app.views import CreatePriorityView
from todolist_app.views import UpdateTodoView
from todolist_app.views import TodoDeleteView
from todolist_app.views import TodoListView
from todolist_app.views import UpdateUserView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', CreateTodoView.as_view(), name='create'),
    path('create_priority/', CreatePriorityView.as_view(), name='create_priority'),
    path('update/<int:pk>', UpdateTodoView.as_view(), name='update'),
    path('update_user/<int:pk>', UpdateUserView.as_view(), name='update_user'),
    path('delete/<int:pk>', TodoDeleteView.as_view(), name='delete'),
    path('', TodoListView.as_view(), name='todo_list'),
]
