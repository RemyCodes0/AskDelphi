from django.urls import path
from . import views
#This section manages the urls
urlpatterns = [
    path('', views.chatbot, name='chatbot'),
    path("del/", views.delete_convers, name="delete"),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
]