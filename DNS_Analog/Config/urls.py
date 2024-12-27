from django.urls import path
from .views import ListView, UpdateViewTask, DeleteView, DetailView, CreateView, searh_list

urlpatterns = [
    path('index/', ListView.as_view(), name='index'),
    path('create/', CreateView.as_view(), name='create'),
    path('update/<int:pk>', UpdateViewTask.as_view(), name='update'),
    path('delete/<int:id>', DeleteView.as_view(), name='delete'),
    path('detail/<int:id>', DetailView.as_view(), name='detail'),
    path('find/', searh_list, name='search'),
]

