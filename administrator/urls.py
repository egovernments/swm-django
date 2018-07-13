from django.urls import path
from . import views
from django.urls import include

app_name = 'administrator'
urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
]
