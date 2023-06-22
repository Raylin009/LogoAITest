import firebase_admin
from firebase_admin import credentials, firestore
import os

cred_path = os.path.abspath(os.path.join(__file__,'..','../firebaseServiceAccountKey.json'))
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)
db = firestore.client()

# def create_firestore_connection (cred_path):
#     cred = credentials.Certificate(cred_path)
#     firebase_admin.initialize_app(cred)
#     return firestore.client()

def write_to_firestore (collection, document, data):
    doc_ref = db.collection(collection).document(document)
    return doc_ref.set(data)

def get_data_from_firestore (collection, document):
    doc_ref = db.collection(collection).document(document)
    retrieved_data = doc_ref.get().to_dict()
    return retrieved_data


    