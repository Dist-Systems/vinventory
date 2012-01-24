from django.test import TestCase
from inventory.models import *

class InventoryViewsTestCase(TestCase):
    '''
    Class variable to load a specific fixture 
    file for this set of tests
    '''
    fixtures = ['inventory_test']

    def test_index(self):
        '''
        Test to exsure that the index page can be 
        loaded with all the correct context elements 
        that are expected to be present
        '''
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('vendor_list' in resp.context)
        self.assertEqual([vendor.pk for vendor in resp.context['vendor_list']], [1])
        vendor1 = resp.context['vendor_list'][0]
        self.assertEqual(vendor1.name, 'Dell Inc.') 

    def test_vm_list(self):
        resp = self.client.get('/inventory/vm/')
        
        # test to ensure that this list view is not broken
        self.assertEqual(resp.status_code, 200)
        # test that the view contains all vms
        # check the pk to ensure that all is as expected
        self.assertEqual([vm.pk for vm in resp.context['vm_list']], [114, 115])
       
    def test_vm_detail(self):
        # Ensure that requests for non-existent vms throw a 404.
        resp = self.client.get('/inventory/vm/1/')
        self.assertEqual(resp.status_code, 404)

        # Ensure that existent vms are viewable.
        resp = self.client.get('/inventory/vm/115/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context['vm'].pk, 115)        
    
    def test_datastore_list(self):
        resp = self.client.get('/inventory/datastore/list/')
         
        # test that the view contains all vms
        # check the pk to ensure that all is as expected
        self.assertEqual([ds.pk for ds in resp.context['dstore_list']], [10, 6])

    def test_datastore_detail(self):
        # Ensure that requests for non-existent datastores throw a 404.
        resp = self.client.get('/inventory/datastore/1/')
        self.assertEqual(resp.status_code, 404)

        # Ensure that existent vms are viewable.
        resp = self.client.get('/inventory/datastore/10/')
        self.assertEqual(resp.status_code, 200)
        vm_1 = resp.context['dstore']
        self.assertEqual(resp.context['dstore'].pk, 10)

    def test_host_list(self):
        resp = self.client.get('/inventory/host/list/')
         
        # test that the view contains all hosts
        # check the pk to ensure that all is as expected
        self.assertEqual([host.pk for host in resp.context['vmhost_list']], [6, 4])

    def test_host_detail(self):
        # Ensure that requests for non-existent hosts throw a 404.
        resp = self.client.get('/inventory/host/1/')
        self.assertEqual(resp.status_code, 404)

        # Ensure that existent hosts are viewable.
        resp = self.client.get('/inventory/host/6/')
        self.assertEqual(resp.status_code, 200)
        vm_1 = resp.context['vmhost']
        self.assertEqual(resp.context['vmhost'].pk, 6)