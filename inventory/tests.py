#from django.utils import unittest
import unittest
from inventory.models import *

# https://docs.djangoproject.com/en/1.3/topics/testing/

class InventoryTestCase(unittest.TestCase):
    def setUp(self):
        self.datastore1 = DataStore.objects.create(name="Storino",capacityMB=1024,freespaceMB=24,filesystemVersion="3.14")

    def testAttributes(self):
        self.assertEqual(self.datastore1.name, "Storino")
        self.assertEqual(self.datastore1.capacityMB, 1024)
        self.assertEqual(self.datastore1.freespaceMB, 24)
        self.assertEqual(self.datastore1.filesystemVersion, "3.14")
