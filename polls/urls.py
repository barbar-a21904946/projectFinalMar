from django.contrib import admin
from django.urls import include, path

from django.urls import path

from . import views
from django.contrib import admin
from django.urls import include, path
urlpatterns = [
    path('', views.index, name='index'),
]



urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]