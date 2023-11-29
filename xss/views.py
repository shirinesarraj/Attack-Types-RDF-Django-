from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import AllowAny



class GreetingView(viewsets.ViewSet):
    permission_classes = [AllowAny]

#XSS Example Vulnerability : Reflected
    def list(self, request):
        queryset = []  # You can specify an appropriate queryset here
        user_input = request.query_params.get('name')
        response_content = f"Hello, {user_input}!"
        return Response({'message': response_content})
    #Test this : Invoke-WebRequest -Uri "http://localhost:8000/greeting/?name=<script>alert('XSS Attack!');</script>"


#XSS Example Vulnerability : Stored
    def create(self, request):
        # Handle POST requests here
        user_input = request.data.get('title')
        # Process and save the input as needed
        response_content = f"Post received with title: {user_input}"
        return Response({'message': response_content})
    #Test this : Invoke-RestMethod -Uri "http://localhost:8000/greeting/" -Method Post -Headers @{"Content-Type"="application/json"} -Body '{"title": "<script>alert(''XSS Attack!'');</script>", "content": "Example content"}'

    



