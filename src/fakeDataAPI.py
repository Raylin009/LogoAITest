import requests

def getFakeData (list, number):
    response = requests.get(f"https://jsonplaceholder.typicode.com/{list}/{number}")
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise requests.exceptions.HTTPError(f"GET request failed with status code {response.status_code}")

