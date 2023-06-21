from test import test_data_in_firestore
from fakeDataAPI import getFakeData
from firebase import writeToFirebase

def main (query, id):
  doc = f'{query}{id}'
  data = getFakeData(query, id)
  writeToFirebase(query, doc, data)
  test_data_in_firestore([query, doc], data)

if __name__ == '__main__':
  main('posts', 6)

  