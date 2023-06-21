from test import test_data_in_firestore
from placeholderAPI_service import get_data_from_placeholder
from firebase_service import write_to_firestore

def main (query, id):
  doc = f'{query}{id}'
  data = get_data_from_placeholder(query, id)
  write_to_firestore(query, doc, data)
  test_data_in_firestore([query, doc], data)

if __name__ == '__main__':
  main('posts', 6)

  