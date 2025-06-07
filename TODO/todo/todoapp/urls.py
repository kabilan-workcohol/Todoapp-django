from django.urls import path
from .views import TodoItemCreateView, TodoItemRetrieveUpdateDestroyView

urlpatterns = [
    path('todo/', TodoItemCreateView.as_view(), name='todo_list_create'),
    path('todo/<int:pk>/', TodoItemRetrieveUpdateDestroyView.as_view(), name='todo_details'),
]

