from django.urls import path
from . import views 

app_name = 'landing_spain'

urlpatterns = [
    path('', view=views.home, name='home'),
]