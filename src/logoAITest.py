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