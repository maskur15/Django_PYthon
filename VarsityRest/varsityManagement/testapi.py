
import requests
print("testing ")
item = requests.get('http://127.0.0.1:8000/students/')

#to delete 
# response = requests.delete('http://127.0.0.1:8000/delete/4')
print(item.json())