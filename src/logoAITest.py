import requests

# Make an API request
response = requests.get('https://jsonplaceholder.typicode.com/todos/1')

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the response as JSON
    data = response.json()

    # Extract and process the required data
    print(data)
else:
    print('Request failed with status code', response.status_code)


import firebase_admin
from firebase_admin import credentials

path = '/Users/raylin/Downloads/logoaitest-firebase-adminsdk-o1d6z-93ce0f5148.json'

cred = credentials.Certificate(path)
firebase_admin.initialize_app(cred)
