import unittest
import os
import firebase_admin
from firebase_admin import credentials, firestore

class FirebaseConnectionTest(unittest.TestCase):
    def test_firebase_connection(self):
        cred_path = os.path.abspath(os.path.join(__file__,'..','../firebaseServiceAccountKey.json'))
        cred = credentials.Certificate(cred_path)
        firebase_admin.initialize_app(cred)

        try:
            db = firestore.client()
            collections = db.collections()
            # If you reached here without any exceptions, the connection was successful
        except Exception as error:
            self.fail(f"Failed to establish a connection with Firestore: {str(error)}")

if __name__ == '__main__':
    unittest.main()

    