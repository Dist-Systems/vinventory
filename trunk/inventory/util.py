from django.db import models
from inventory.models import VirtualMachine, VMHost, DataStore
import sys,os,csv

def openDataSource(file_path, names):
  stream = open(file_path)
  dataReader = csv.DictReader((stream), fieldnames=names)
  
  # Don't need the header, because the names don't match
  dataReader.next()
  return dataReader

def createVirtualMachines(dataStream, print=False):
  for row in dataStream:
    vm, created = VirtualMachine.objects.get_or_create(name=row['Name'])
    if created:
      # Only proceed if the virtual host exists
      if VMHost.objects.filter(name = row['VMHost']):
          # Create a new virtual machine
          vm      = VirtualMachine()
          vm.name = row['Name']
      else:
          msg = 'Virtual host({0}) does not exist'.format(row['VMHost'])
          # http://docs.python.org/tutorial/errors.html
          raise RuntimeError(msg)

      # Populate the boolean value for the power state (any sting is True)
      if row['PowerState'].endswith('Off'):
          row['PowerState'] = False
      vm.powerState = row['PowerState']
      vm.cpuCount   = row['NumCpu']
      vm.memoryMB   = row['MemoryMB']
      vm.host       = VMHost.objects.get(name = row['VMHost'])
      vm.save()
      print '({0}) created'.format(row['Name']),

    else:
        # The vitual machine exists, assign it to 'vm'
        print '({0}) already exists'.format(row['Name']),
        vm = VirtualMachine.objects.get(name=row['Name'])

    # The following is performed on existing or newly created VMs
    # Seek out the data store, this eliminates blanks
    for d in row['Datastore'].split(' '):
        ds  = DataStore.objects.get(name = d)
        vm.datastore.add(ds)
        print '  added datastore ({0})'.format(d)

    # Name is the identifier, so we can't update it
    # vm.name       = row['Name']
    # Populate the boolean value for the power state (any sting is True)
    if row['PowerState'].endswith('Off'):
        row['PowerState'] = False
    vm.powerState = row['PowerState']
    vm.cpuCount   = row['NumCpu']
    vm.memoryMB   = row['MemoryMB']
    vm.notes      = row['Notes']
    vm.host       = VMHost.objects.get(name = row['VMHost'])
    vm.save()
  print 'updated'