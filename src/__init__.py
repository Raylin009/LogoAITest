import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

path = '/Users/raylin/Downloads/logoaitest-firebase-adminsdk-o1d6z-93ce0f5148.json'

cred = credentials.Certificate(path)
firebase_admin.initialize_app(cred)



# Get a Firestore client
db = firestore.client()

# Define data to be stored
data = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}

# Add the data to a document in a collection
doc_ref = db.collection('users').document('user1')
doc_ref.set(data)