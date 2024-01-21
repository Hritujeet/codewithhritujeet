from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('post/<str:slug>', views.post),
]
