

from rest_framework import generics
from .models import UserProfile
from .serializers import UserProfileSerializer
from django.http import JsonResponse

class UserProfileListCreateView(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    def post(self, request, *args, **kwargs):
        
        response_data = {'message': 'CSRF Attack Successful'}
        return JsonResponse(response_data,status=200)