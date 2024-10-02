
# urls paths for todo ap django

from django.urls import path
from . import views

urlpatterns = [
    path('', views.TodoDetail, name='todo_list'),
    path('<int:pk>/', views.TodoDetail, name='todo_detail'),
    # post
    path('post/', views.TodoPost, name='todo_post'),
    path('put/<int:pk>/', views.TodoPut, name='todo_put'),
    path('delete/<int:pk>/', views.TodoDelete, name='todo_delete')
]