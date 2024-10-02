# urls for API resolver


from django.urls import path

from . import views

urlpatterns = [
    path('api/<str:question>/', views.ApiDetail),    ]

