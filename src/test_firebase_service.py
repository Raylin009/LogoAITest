import unittest
import os
import json
import firebase_service
from firebase_service import write_to_firestore, get_data_from_firestore

class FirebaseConnectionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.collection, cls.document = 'posts', '6'
        sample_data_address = os.path.abspath(os.path.join(__file__,'..','../sampleData.json'))
        with open(sample_data_address, 'r', encoding="utf8") as file:
            cls.sample_data = json.load(file)

    def test_firebase_connection(self):
        try:
            collections = firebase_service.db.collections()
        except Exception as error:
            self.fail(f"Failed to establish a connection with Firestore: {str(error)}")
    def test_write_to_firestore(self):
        document_id = write_to_firestore(self.collection, self.document, self.sample_data)
        self.assertIsNotNone(document_id)
    def test_get_data_from_firestore(self):
        actual_data = get_data_from_firestore(self.collection, self.document)
        self.assertEqual(self.sample_data, actual_data)

if __name__ == '__main__':
    unittest.main()