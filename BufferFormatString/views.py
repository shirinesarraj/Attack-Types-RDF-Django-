from django.http import HttpResponse


#BufferOverFlow Vulnerablity
def vulnerable_function1(request, input_string):
    buffer_size = 10
    buffer = bytearray(10)
    if len(input_string) > buffer_size:
        return HttpResponse("Buffer overflow detected!")
    for i in range(len(input_string)):
        buffer[i] = input_string[i]
    return HttpResponse(str(buffer))
#Test: http://yourdomain.com/vulnerable1/?input_string=AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
#prevention of BufferOverflow Vulnerabilty:
def safer_function1(request, input_string):
    buffer_size = 10
    buffer = bytearray(10)
    if not isinstance(input_string, str):
        return HttpResponse("Invalid input type. Please provide a valid string.")
    for i in range(min(len(input_string), buffer_size)):
        buffer[i] = ord(input_string[i])  # Use ord() to get the ASCII value of the character
    return HttpResponse(str(buffer))

#test : http://localhost:8000/BufferFormatString/safer_function1/Spec!@alChars/



#StringFormat
from django.http import HttpResponse
def vulnerable_function2(request, input_string):
    # Simulate a situation where the input is used in a format string
    message = f"User input: {input_string}"
    # In a vulnerable scenario, this could be used as a format string without proper validation
    formatted_message = message.format(input_string)
    return HttpResponse(formatted_message)
#Test : http://localhost:8000/BufferFormatString/vulnerable2/AAAA*p%5E%C3%B9ld,hqhbja/
#prevention of uncontrolled string format : 
from django.http import HttpResponse
def safer_function2(request, input_string):
    # Use f-string with placeholders to include user input
    safe_message = f"User input: {input_string}"
    return HttpResponse(safe_message)
#prevention test : http://localhost:8000/BufferFormatString/safer_function2/AAAA*p%5E%C3%B9ld,hqhbja%n
# output: AAAA*p^ùld,hqhbja%n