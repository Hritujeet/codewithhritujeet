from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('login', views.handleLogin),
    path('logout', views.handleLogout),
    path('signup', views.signup),
    path('about', views.about),
    path('contact', views.contact),
]
