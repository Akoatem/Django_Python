# creating mapping that will work with the calc app ffrom ako urls.py mapping

from django.urls import path
from . import views

#mapping here
urlpatterns = [
    path('', views.home, name='home'),
    path('add', views.add, name='add')
    
]
