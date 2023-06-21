from firebase import get_data_from_firestore, write_to_firestore
from fakeDataAPI import get_data_from_placeholder
import unittest

class TestWriteToDatabase(unittest.TestCase): 
  def setup(self):
    print('setUp')
    # get fake datat
    fake_data = get_data_from_placeholder('posts', 6)
    # write fake data to firestore
    write_to_firestore('posts', f'posts{6}', fake_data)
  
  def teardown(self):
    print ('tearDown')

  def test_data(self):
    # get fake datat
    fake_data = get_data_from_placeholder('posts', 6)
    # retrieve data from firestore
    firestore_data = get_data_from_firestore('posts', 6)
    # asssert data are correct
    self.assertEqual(firestore_data, fake_data)


def test_data_in_firestore (quary_info, expected_data):
  [collection, doc] = quary_info
  firebase_data = get_data_from_firestore(collection, doc)

  assert firebase_data == expected_data, "Data mismatch in Firestore"
  print('pass')
