"""ceo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name="redirect"),
    path('events/', include('events.urls')),
    path('polls/', include('polls.urls')),
    path('accounts/',include('accounts.urls')),
    path('administrator/',include('administrator.urls')),
    path('notification/',include('notification.urls')),
    path('nearby/',include('nearby.urls')),
    path('cal/',include('cal.urls')),
    path('notice/',include('notice.urls')),
    path('news/',include('news.urls')),
    #path('evecal/',include('eventcalendar.urls')),

    path('request/', include('request.urls')),
    # path('nearme/', include('nearme.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
admin.site.site_header = 'Administration'
admin.site.site_title = 'CEO'
