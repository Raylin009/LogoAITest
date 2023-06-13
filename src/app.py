from fakeDataAPI import getFakeData
from firebase import writeToFirebase
from test import test_data_in_firestore

def experiment (query, id):
  doc = f'{query}{id}'
  data = getFakeData(query, id)
  writeToFirebase(query, doc, data)
  test_data_in_firestore([query, doc], data)

experiment('posts', 6)

