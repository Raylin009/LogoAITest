from firebase import getDataFromFirebase

def test_data_in_firestore (quary_info, expected_data):
  [collection, doc] = quary_info
  firebase_data = getDataFromFirebase(collection, doc)

  assert firebase_data == expected_data, "Data mismatch in Firestore"
  print('pass')
