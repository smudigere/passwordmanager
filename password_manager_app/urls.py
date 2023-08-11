from django.urls import path
from . import views


urlpatterns = [
    path('passwords/', views.password_list, name='password_list'),
    path('add_password/', views.add_password, name='add_password'),
    path('get_password/', views.get_password, name='get_password'),
]
