import requests

# API endpoint for creating users
create_user_url = 'http://127.0.0.1:8000/api/users/'

# JSON data representing the new user
# JSON data representing the new user
new_user_data = {
    "id":1,
    "name": "John Doe",
    "phone": "11111111111",
    "password": "pass1",
    "email": "john_doe@gmail.com"
}

# Make a POST request to create the user
response = requests.post(create_user_url, json=new_user_data)

# Check the response status
if response.status_code == 201:
    print("User created successfully.")
else:
    print("Failed to create user. Status code:", response.status_code)
    print("Response:", response.json())
