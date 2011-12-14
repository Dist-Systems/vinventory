from django.utils import unittest
from inventory.models import *

class InventoryTestCase(unittest.TestCase):
    def setUp(self):
        self.datastore1 = DataStore.objects.create(name="Storino",capacityMB=1024,freespaceMB=24,filesystemVersion="3.14")

    def testAttributes(self):
        self.assertEqual(self.datastore1.name, "Storino")
        self.assertEqual(self.datastore1.capacityMB, 1024)
        self.assertEqual(self.datastore1.freespaceMB, 24)
        self.assertEqual(self.datastore1.filesystemVersion, "3.14")
