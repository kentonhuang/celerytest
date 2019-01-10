from django.urls import path

from . import views

app_name = "articles"

urlpatterns = [
  path('articles/', views.ListTodo.as_view()),
  path('articles/<int:pk>', views.DetailTodo.as_view()),
]