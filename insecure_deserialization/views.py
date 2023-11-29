from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework.response import Response
from rest_framework import status 
import time


# Data Tempering
class BlogPostUpdateView(generics.UpdateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    authentication_classes = []  # Allow any authentication
    permission_classes = [AllowAny]  # Allow any permission
#testing with cmd : C:\Users\hp>curl -X PATCH http://localhost:8000/update-post/1/ -H "Content-Type: application/json" -d "{\"title\": \"Malicious Title\", \"content\": \"SomeMaliciousContent\"}"
#output :{"id":1,"title":"Malicious Title","content":"SomeMaliciousContent"}

#Mitigations Strategies:
# def validate_content(self, value):
#         # Implement validation logic to ensure content is safe
#         if contains_malicious_code(value):
#             raise serializers.ValidationError("Malicious content detected.")
#         return value


#Denial Of Service



class ExpensiveTaskView(generics.CreateAPIView):
    def perform_expensive_task(self):
        # Simulate a computationally expensive task with a delay
        time.sleep(5)  # Sleep for 5 seconds to simulate a delay
        return "Task completed successfully!"

    def create(self, request, *args, **kwargs):
        # Perform the expensive task
        result = self.perform_expensive_task()
        return Response({'result': result}, status=status.HTTP_200_OK)
    

#save this into stress_test.bat : @echo off
# set ENDPOINT=http://localhost:8000/expensive-task/
# rem Adjust the number of requests as needed
# set NUM_REQUESTS=100
# rem Loop through the requests
# for /L %%i in (1, 1, %NUM_REQUESTS%) do (
#     curl -X POST %ENDPOINT% -H "Content-Type: application/json" -d "{\"data\": \"some_data\"}"
#     rem Add a delay between requests (adjust as needed)
#     timeout /nobreak /t 1
# )
# echo Stress test complete
#test : navigate to C:\Users\hp\Desktop>stress_test.bat and u'll see the result
    


