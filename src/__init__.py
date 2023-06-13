import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os


cred_path = os.path.abspath(os.path.join(__file__,'..','../firebaseServiceAccountKey.json'))
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)



# Get a Firestore client
db = firestore.client()

# Define data to be stored
data = {
    'name': 'test new path for cred',
    'age': 30,
    'city': 'New York'
}

# Add the data to a document in a collection
doc_ref = db.collection('users').document('user7')
doc_ref.set(data)

# print(os.path.abspath(os.path.join(__file__,'..','../firebaseServiceAccountKey.json')))