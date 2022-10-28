# User-Auth-DRF

# User API (Rest Framework)

## Testing Commands

1. Clone Repository from [GitHub](https://github.com/AfaqShuaib09/User-Auth-DRF) `git clone https://github.com/AfaqShuaib09/User-Auth-DRF.git`
2. Change your current present working directory (pwd) to `cd User-Auth-DRF`
3. Change your current branch from main to user_auth_drf : `git checkout user_auth_drf`
4. Create python virtual environment `python3 -m venv env`
5. Activate the virtual environment: `source env/bin/activate`
6. Install dependencies: ` pip install -r requirements.txt`
7. Navigate to user_project directory `cd user_api`
8. Make migrations `python3 manage.py makemigrations`
9. Apply migrations `python3 manage.py migrate`
   (you can skip the 8 command here)
10. Create superuser: `python manage.py createsuperuser`
11. Run django App: `python3 manage.py runserver`

> Custom Permission added to the profile model so that only the user can edit (partially or fully) or delete their own profile

## Register User

### Request Type: POST

> URL: http://localhost:8000/api/register/

> Body:

```bash
{
    "username": "Afaqboi",
    "email": "afaq.shoaib09@gmail.com"
    "password": "asdqweasd"
}
```

<img width="1128" alt="image" src="https://user-images.githubusercontent.com/78806673/184858596-fa07106f-9c5f-42ed-a782-c28aa9e79068.png">

> Response Type: JSON

> Status Code: 201 Created

Returns the created user object.

## Login User

### Request Type: POST

> URL: http://localhost:8000/api/login/

> Body:

```bash
{
    "username": "Afaqboi",
    "password": "asdqweasd"
}
```

<img width="1135" alt="image" src="https://user-images.githubusercontent.com/78806673/184860108-9bac7921-6ee1-465a-842a-906d91bf652c.png">

> Response Type: JSON

> Status Code: 200 OK

Returns the authetication token.

## Logout User

### Request Type: POST

> URL: http://localhost:8000/api/logout/

(In Headers)

> Authorization: Token <token>

<img width="1132" alt="image" src="https://user-images.githubusercontent.com/78806673/184860852-8a7284e3-f5ac-450b-a347-9d1017295d93.png">

> Status Code: 204 No Content
> (Means the server has successfully processed the request and has no response to send back to the client)

## Password Reset

### Request Type: POST

> URL: http://localhost:8000/api/password_reset/

> Body:

```bash
{
    "email": "afaq.shoaib09@gmail.com"
}
```

<img width="1130" alt="image" src="https://user-images.githubusercontent.com/78806673/184863054-085cbf3f-4f8e-4093-b21e-b2a1fb833c48.png">

> Response status code: 200 OK

> Password reset token printed in the console.

Copy the token and pass the token x-www-form-urlencoded in the body along with the new password.

<img width="1143" alt="image" src="https://user-images.githubusercontent.com/78806673/184864228-016824c4-ce1c-4ac5-a037-12a73f073fcd.png">

> Response status code: 200 OK

## Permissions Added to Viewset

Register User : AllowAny (Anyone can register)

Login User : AllowAny (Anyone can login having valid credentials)

Logout User : knox_auth (Only authenticated users can logout and delete their token)

User Detail : isAuthenticated (Only authenticated users can view their details

1. Get -> id
2. Get -> list

Authentication Credentials not provided Error if token is not provided in the header.
<img width="1123" alt="image" src="https://user-images.githubusercontent.com/78806673/184865689-aa5e7035-fab2-46fb-a921-73006ed28b54.png">

When token is provided in the header, the user is authenticated.

### Request Type: GET

> URL: http://localhost:8000/api/users/

(List of all users)
<img width="1157" alt="image" src="https://user-images.githubusercontent.com/78806673/184866645-391a3b77-c9cb-491d-a5af-0ad3ef80db98.png">

> URL: http://localhost:8000/api/users/user_id/

(Detail of a user)

<img width="1129" alt="image" src="https://user-images.githubusercontent.com/78806673/184867134-78cdabac-1012-44e0-b3d0-e9bc4192f0a4.png">

## Profile CRUD

## Profile Detail

### Request Type: Get

> URL: http://localhost:8000/api/profiles/

<img width="1141" alt="image" src="https://user-images.githubusercontent.com/78806673/184872839-82a8d6cd-17a5-489a-a556-10902eb23b9e.png">

> Response Type: JSON

> Status Code: 200 OK

## Profile Detail by username

### Request Type: Get

> URL: http://localhost:8000/api/profiles/username/

> Response Type: JSON

<img width="1143" alt="image" src="https://user-images.githubusercontent.com/78806673/184873273-905fb7ac-d5eb-4bc7-a6ee-d97b0d3b48f2.png">

## Create User Profile

### Request Type: POST

> URL: http://localhost:8000/api/profiles/

> Body:

```bash
{
        "username": "Afaqboi",
        "full_name": "M Afaq Shuaib",
        "cnic": "35202-2577833-6",
        "contact_number": "+923064416475",
        "address": "27 Huma Block",
        "gender": "Male",
        "country": "PK"
}
```

<img width="1138" alt="image" src="https://user-images.githubusercontent.com/78806673/184872223-da80a0c1-5d4f-4f00-9979-676aa5cf600a.png">

## Profile Update

### Request Type: PATCH

> URL: http://localhost:8000/api/profiles/username/

> Body:

```bash
{
    "full_name": "Muhammad Afaq",
    "cnic": "35202-2577800-6",
    "contact_number": "+923064416400",
    "address": "34 Huma Block AIT Lahore",
    "gender": "Male",
    "country": "PK"
}
```

<img width="1133" alt="image" src="https://user-images.githubusercontent.com/78806673/184874016-344c7435-8fbf-4ab1-a74b-69d36e2c50d7.png">

> Status Code : 200 OK

## Profile partial update

### Request Type: PATCH

> URL: http://localhost:8000/api/profiles/username/

Body:

```
{
    "contact_number": "+923245227602",
    "address": "34 Huma Block Allama Iqbal Town"
}

```

Only the fields that are provided in the body will be updated.

<img width="1139" alt="image" src="https://user-images.githubusercontent.com/78806673/184874811-4ef1bbda-127a-4e1c-b7a6-f8bef7cb1647.png">

## Profile Delete

### Request Type: DELETE

> URL: http://localhost:8000/api/profiles/<username>/

> Status Code: 204 No Content

<img width="1137" alt="image" src="https://user-images.githubusercontent.com/78806673/184875669-ee1a3aa5-e4eb-49fc-8df6-a18a8dd60f88.png">
