# Credicxo_API
## Requirements for the Project:

asgiref==3.2.10
astroid==2.4.2
Django==3.1.2
django-rest-auth==0.9.5
django-rest-passwordreset==1.1.0
djangorestframework==3.12.1
djangorestframework-jwt==1.11.0
isort==5.6.0
lazy-object-proxy==1.4.3
mccabe==0.6.1
psycopg2==2.8.6
PyJWT==1.7.1
pylint==2.6.0
pytz==2020.1
six==1.15.0
sqlparse==0.4.1
toml==0.10.1
wrapt==1.12.1

## API's  
#### List User  

**GET** 127.0.0.1:8000/api/users/  
**Headers**  
**Authorization**  
JWT <eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6ImFyanVuMUBnbWFpbC5jb20iLCJleHAiOjE2MDIxNTIzODcsImVtYWlsIjoiYXJqdW4xQGdtYWlsLmNvbSJ9.6gm-67-25yIpkt7q5XLA01nkYR0jFV1fvDhgl3ayYg4>  
**Content-Type**  
application/json  

#### Create User  
**POST** 127.0.0.1:8000/api/users/  
**Headers**  
**Authorization**  
JWT <eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6ImFyanVuMUBnbWFpbC5jb20iLCJleHAiOjE2MDIxNTIzODcsImVtYWlsIjoiYXJqdW4xQGdtYWlsLmNvbSJ9.6gm-67-25yIpkt7q5XLA01nkYR0jFV1fvDhgl3ayYg4>
**Content-Type**  
application/json  
**Body**  
>{  
>   "email": "abc@gmail.com",  
>    "password": "yourpassword",  
>    "profile": {  
>       "group":3  
>    }  
>} 
#### Delete User
**POST** 127.0.0.1:8000/api/users/1/    
**Headers**  
**Authorization**  
JWT <eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6ImFyanVuMUBnbWFpbC5jb20iLCJleHAiOjE2MDIxNTIzODcsImVtYWlsIjoiYXJqdW4xQGdtYWlsLmNvbSJ9.6gm-67-25yIpkt7q5XLA01nkYR0jFV1fvDhgl3ayYg4>

#### Password-Reset  
**POST** 127.0.0.1:8000/api/password_reset/      
**Headers**  
**Authorization**  
JWT <eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6ImFyanVuMUBnbWFpbC5jb20iLCJleHAiOjE2MDIxNTIzODcsImVtYWlsIjoiYXJqdW4xQGdtYWlsLmNvbSJ9.6gm-67-25yIpkt7q5XLA01nkYR0jFV1fvDhgl3ayYg4>
**Body**  
>{  
>"email":abc@gmail.com  
>}  

#### Password-Reset Confirm 
**POST** 127.0.0.1:8000/api/password_reset/confirm/      
**Headers**  
**Authorization**  
JWT <eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6ImFyanVuMUBnbWFpbC5jb20iLCJleHAiOjE2MDIxNTIzODcsImVtYWlsIjoiYXJqdW4xQGdtYWlsLmNvbSJ9.6gm-67-25yIpkt7q5XLA01nkYR0jFV1fvDhgl3ayYg4>
**Body**  
>{  
>"password":"newpassword",  
>"token":"emailtoken received in gmail"  
>}  





