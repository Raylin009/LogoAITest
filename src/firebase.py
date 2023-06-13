import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os

cred_path = os.path.abspath(os.path.join(__file__,'..','../firebaseServiceAccountKey.json'))
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)
db = firestore.client()

def writeToFirebase (collection, document, data):
    doc_ref = db.collection(collection).document(document)
    doc_ref.set(data)

def getDataFromFirebase (collection, document):
    doc_ref = db.collection(collection).document(document)
    retrieved_data = doc_ref.get().to_dict()
    return retrieved_data
    
# print (getDataFromFirebase('users', 'user8'))