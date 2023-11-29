from django.urls import path
from .views import get_user_data,read_file

urlpatterns = [
    # path('get_user_data/', get_user_data, name='user_data'),
    path('get_user_data/', get_user_data, name='get_user_data'),
    path('read_file/', read_file, name='read_file'),


]
