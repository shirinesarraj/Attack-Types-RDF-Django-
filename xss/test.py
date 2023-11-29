# yourapp/tests.py
from django.test import TestCase
from django.urls import reverse
from rest_framework import status

class GreetingViewTests(TestCase):
    def test_greeting_view(self):
        user_input = '<script>alert("XSS Attack!");</script>'
        url = reverse('greeting-view')  # Replace 'greeting-view' with the actual name or path

        # Assuming your view allows unauthenticated access, no need for authentication in the test
        response = self.client.get(url, {'name': user_input})

        # Check that the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that the user input is properly escaped or sanitized in the response
        self.assertNotContains(response, user_input)
