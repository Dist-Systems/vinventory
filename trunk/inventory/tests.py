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
        self.assertEqual(resp.status_code, 200)
        self.assertEqual([vm.pk for vm in resp.context['vm_list']], [114, 115])
       
    def test_vm_detail(self):
        # Ensure that non-existent vms throw a 404.
        resp = self.client.get('/inventory/vm/1/')
        self.assertEqual(resp.status_code, 404)
        # Ensure that existent vms are viewable.
        resp = self.client.get('/inventory/vm/115/')
        self.assertEqual(resp.status_code, 200)
        vm_1 = resp.context['vm_list'][0]
        self.assertEqual(resp.context['vm_list'][0].pk, 115)        

    def test_datastores(self):
        count = len(DataStore.objects.all())
        assert(count == 2)
