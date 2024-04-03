import requests

# Base URL for your API
base_url = 'http://localhost:8000/api/'
token = 'cf20d38f60ba2e9762684b8b2426d4bc9f18a526'
#token =5056bb40046937a7f3665fd647feac1ea4005310
#{"name":"Hasan","Phone": "2029292","email":"hasan@gmail.com","password":"password"}
def register_user(name, phone, email, password):
    url=base_url+'register/'
    data = {
        'name': name,
        'phone': phone,
        'email': email,
        'password': password
    }
    response = requests.post(url, json=data)
    if response.status_code == 201:
        print("User registered successfully!",response.json())
    else:
        print("Failed to register user:", response.text)

# Example usage
#register_user("John mok", "1234567890", "john@example.com", "secretpassword")
def get_all_users(token='5056bb40046937a7f3665fd647feac1ea4005310'):
    base_url = 'http://127.0.0.1:8000/api/'  # Update with your base URL
    url = base_url + 'users/'
    # Define the headers with the authentication token
    headers = {'Authorization': f'Token {token}'}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        users = response.json()
        print("All users:")
        print(users)
    else:
        print("Failed to retrieve users:", response.text)

# Call the function to retrieve all users
def login(email,password):
    url = base_url+'login/'
    data={
          'email':email,
          'password':password
          }
    response = requests.post(url, data=data)

    # Check the response status code
    if response.status_code == 200:
        # If successful, print the token
        print("Login successful!")
        print("Token:", response.json()['token'])
    else:
        # If not successful, print the error message
        print("Login failed:", response.json()['error'])
#login('john@example.com','secretpassword')


base_url = 'http://127.0.0.1:8000/api/'

# Function to make a POST request and print the response
def rate_book(data,token):
    # Define the headers with the authentication token
    headers = {'Authorization': 'Token '+token}
    response = requests.post(base_url + 'rate/', json=data,headers=headers)
    print('POST request to '+base_url+'rate/')
    print('Response:', response.status_code)
    print(response.json())
    print()
def test_post(endpoint, data):


    response = requests.post(base_url + endpoint, json=data)
    print(f'POST request to {base_url + endpoint}')
    print('Response:', response.status_code)
    print(response.json())
    print()

def test_get(endpoint):
    response = requests.get(base_url + endpoint)
    print(f'GET request to {base_url + endpoint}')
    print('Response:', response.status_code)
    print(response.json())
    print()
new_rating={
"book_id":1,
"user_rating:": 5
}
#test_get('books/')

# get_all_users()
#rate_book(new_rating,token=token)

def rate_book():
    headers = {'Authorization': f'Token {token}'}
    # Define the base URL of your API
    base_url = 'http://127.0.0.1:8000/api/'
    # Define the endpoint for rating a book
    endpoint = 'rate_book/'
    # Define the request data
    data = {"book_id":2,"user_rating":3.0}
    response = requests.post(base_url + endpoint, data=data,headers=headers)
    print(response.status_code)
    print(response.json())
def add_book(data):
    headers = {'Authorization': f'Token {token}'}
    # Define the base URL of your API
    base_url = 'http://127.0.0.1:8000/api/'
    # Define the endpoint for rating a book
    endpoint = 'add_book/'
    response = requests.post(base_url + endpoint, data=data,headers=headers)
    print(response.status_code)
    print(response.json())

# Call the function with the book ID and user rating
#rate_book()
# test_get('book/1')
# test_get('ratings/')
new_book={
"name": "Python for dummy",
"genre":"programming",
"book_rating":"Good",
"release_date":"2019-12-1"
}
#add_book(new_book)
get_all_users(token=token)
#login('hasan@gmail.com','password')
#register_user("maskur","01783015123","maskur@gmail.com","password")
#add_book(new_book)
rate_book()