# We need the path

from django.urls import path
from . import views

# django recognizes path urls when they are
#defined in the variable 'urlpatterns'.

app_name = 'myread-urls'
urlpatterns = [
    path('', views.home_page, name='home-page')
    
]