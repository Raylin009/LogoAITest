from firebase import getDataFromFirebase, writeToFirebase
from fakeDataAPI import getFakeData
import unittest

class TestWriteToDatabase(unittest.TestCase): 
  def setup(self):
    print('setUp')
    # get fake datat
    fake_data = getFakeData('posts', 6)
    # write fake data to firestore
    writeToFirebase('posts', f'posts{6}', fake_data)
  
  def tearDown(self):
    print ('tearDown\n')
    

  def test_data(self):
    # get fake datat
    fake_data = getFakeData('posts', 6)
    # retrieve data from firestore
    fireStore_data = getDataFromFirebase('posts', 6)
    # asssert data are correct
    self.assertEqual(fireStore_data, fake_data)


def test_data_in_firestore (quary_info, expected_data):
  [collection, doc] = quary_info
  firebase_data = getDataFromFirebase(collection, doc)

  assert firebase_data == expected_data, "Data mismatch in Firestore"
  print('pass')
