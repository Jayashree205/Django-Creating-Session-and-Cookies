from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login_view'),  # Updated to match view name
    path('welcome/', views.welcome_view, name='welcome_view'),  # Updated to match view name
]
