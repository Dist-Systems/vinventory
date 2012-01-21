#from django.utils import unittest
#import unittest
import os
from django.test import TestCase
from django.core.management import call_command
from inventory.models import Server, DataStore, VMHost, VirtualMachine, Vendor, IpAddress
from inventory.utils import createDataStores, createVirtualHosts, createVirtualMachines, createIPs, openDataSource
from datetime import datetime

# https://docs.djangoproject.com/en/dev/topics/testing/
# https://docs.djangoproject.com/en/1.3/topics/testing/

# CONSTANTS
CAPACITYMB=1024
FREESPACEMB=2
CPUNUM=1
DATETIME = datetime(2011, 12, 15, 21, 2, 34, 863905)

# Utility methods defined here and used throughout the test cases
class Util:
    @staticmethod
    def new_vendor(name, website=''):
      vendor = Vendor(name=name, website=website)
      vendor.save()
      return vendor

    @staticmethod
    def new_server(name, vendor):
      notes = '[default notes]'
      capMB = CAPACITYMB
      cpuNum = CPUNUM
      purchased = DATETIME
      server = Server(name=name, notes=notes, vendor=vendor, capacityMB=capMB, cpuCount=cpuNum, purchased=purchased)
      server.save()
      return server

    @staticmethod
    def new_datastore(name):
      ds = {}
      ds['name']             = name
      ds['capacityMB']       = CAPACITYMB
      ds['freespaceMB']      = FREESPACEMB
      ds['filesystemVersion']= "3.14"
      datastore = DataStore.create(**ds)
      datastore.save()
      return datastore


class InventoryTestAttributesCase(TestCase):
    # Perhaps we should consider http://docs.python.org/library/functions.html#hasattr
    # for these simple tests
    fixtures = ['ds']
    def setUp(self):
        call_command('loaddata', 'inventory')
        self.vendor = Util.new_vendor(name='Vendorino', website='http://venderino.com')
        self.datastore1 = Util.new_datastore("Storino")
        self.server1 = Util.new_server('Serverino', self.vendor)

    def testVendorAttributes(self):
        self.assertEqual(self.vendor.name, "Vendorino")

    def testServerAttributes(self):
        self.assertEqual(self.server1.name, "Serverino")
        self.assertEqual(self.server1.capacityMB, CAPACITYMB)
        self.assertEqual(self.server1.vendor, self.vendor)
        self.assertEqual(self.server1.purchased, DATETIME)

    def testDataStoreAttributes(self):
        self.assertEqual(self.datastore1.name, "Storino")
        self.assertEqual(self.datastore1.capacityMB, CAPACITYMB)
        self.assertEqual(self.datastore1.freespaceMB, FREESPACEMB)
        self.assertEqual(self.datastore1.filesystemVersion, "3.14")