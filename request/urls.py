from django.urls import path

from . import views

app_name = 'request'
urlpatterns = [
	path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('<int:request_id>/', views.detail, name='detail'),
    path('create/<int:point_id>', views.create, name='create'),
    path('<int:event_id>/attend/', views.attend, name='attend'),
]