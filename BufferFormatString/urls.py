
from django.urls import path
from .views import vulnerable_function1, vulnerable_function2,safer_function2,safer_function1

urlpatterns = [
    path('vulnerable1/<str:input_string>/', vulnerable_function1, name='vulnerable_function1'),
    path('vulnerable2/<str:input_string>/', vulnerable_function2, name='vulnerable_function2'),
    path('safer_function1/<str:input_string>/', safer_function1, name='safer_function1'),
    path('safer_function2/<str:input_string>/', safer_function2, name='safer_function2'),

    

]
