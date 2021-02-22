from django.urls import path
from . import views

urlpatterns = [
    path('message/', views.MessageApiView.as_view()),
    path('message/create', views.MessageCreateApiView.as_view()),
]
