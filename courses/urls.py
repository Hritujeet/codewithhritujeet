from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('tutorial/<str:slug>', views.course),
]
