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


    def test_datastores(self):
        count = len(DataStore.objects.all())
        assert(count == 2)
