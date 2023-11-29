"""
URL configuration for AttackTest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from corscsrf.views import UserDataView
from insecure_deserialization.views import BlogPostUpdateView,ExpensiveTaskView
from Sql.views import get_user_data
from Sql.views import get_user_data,read_file






urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include(router.urls)),
    path('BufferFormatString/', include('BufferFormatString.urls')),
    path('corscsrf/', include('corscsrf.urls')),
    path('update-post/<int:pk>/', BlogPostUpdateView.as_view(), name='update_post'),
    path('api/user_data', UserDataView.as_view(), name='user_data'),
    path('expensive-task/', ExpensiveTaskView.as_view(), name='expensive_task'),
    #path('execute_command/', execute_command, name='execute_command'),
    path('get_user_data/', get_user_data, name='get_user_data'),  # Add this line
    path('read_file/', read_file, name='read_file'),


    path('testsql/', include('Sql.urls')),


]

