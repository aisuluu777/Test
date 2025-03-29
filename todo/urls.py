from django.urls import path

from . import views

urlpatterns = [
    path('', views.TodoListApiView.as_view()),
    path('<int:id>/', views.TodoDetailApiView.as_view())
]