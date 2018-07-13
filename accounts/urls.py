from django.urls import path
from . import views
from django.urls import include
from django.contrib.auth.views import login, logout

app_name = 'accounts'
urlpatterns = [
    path('login/',login,name='login'),
    path('register/',views.my_view,name='register'),
    path('editpref/',views.editpref,name='prefedit')
]
