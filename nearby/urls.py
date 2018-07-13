from django.urls import path
from . import views
app_name = 'nearby'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('new/<type>', views.maps, name = 'map'),
    path('<type>/', views.type, name = 'type')
]