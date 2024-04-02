import requests

# Base URL for the API
base_url = 'http://127.0.0.1:8000/api/'

# Function to make a POST request and print the response
def test_post(endpoint, data):
    response = requests.post(base_url + endpoint, json=data)
    print(f'POST request to {base_url + endpoint}')
    print('Response:', response.status_code)
    print(response.json())
    print()

# Function to make a GET request and print the response
def test_get(endpoint):
    response = requests.get(base_url + endpoint)
    print(f'GET request to {base_url + endpoint}')
    print('Response:', response.status_code)
    print(response.json())
    print()

# Test creating a new user
new_user_data = {
    "name": "John Malik",
    "phone": "456",
    "password": "paspoi1",
    "email": "poi@gmail.com"
}
#test_post('user/', new_user_data)

# Test retrieving a specific user
#test_get('user/5')

# Test retrieving all books
#test_get('books/')

# Test rating a book
# new_rating_data = {
#     "user_id": 1,
#     "book_id": 1,
#     "user_rating": 5.0
# }
# test_post('rate/', new_rating_data)
# Function to make a GET request and print the response
def test_get_all_users():
    response = requests.get(base_url + 'users/')
    print(f'GET request to {base_url + "users/"}')
    print('Response:', response.status_code)
    print(response.json())
    print()

# Test retrieving all users
#test_get_all_users()