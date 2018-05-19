from django.urls import path
from .views import *

urlpatterns = [
	path('', index, name='index'),
	path('<room_name>/', room, name='room')
]