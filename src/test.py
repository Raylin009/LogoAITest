from firebase import getDataFromFirebase
from fakeDataAPI import getFakeData

def test_data_in_firestore (quary_info, expected_data):
  [collection, doc] = quary_info
  firebase_data = getDataFromFirebase(collection, doc)

  assert firebase_data == expected_data, "Data mismatch in Firestore"

# test_data_in_firestore(['users', 'user8'], getFakeData('todos', 1))