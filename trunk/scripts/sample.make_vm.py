#change these variables to suit your environment
username = 'user'

# Full path and name to your csv file
csv_filepathname="/Users/{0}/Desktop/vinventory/data/VirtualMachine.csv".format(username)

# Full path to your django project directory
your_djangoproject_home="/Users/{0}/Desktop/vinventory/".format(username)

import sys,os
sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from inventory.models import VirtualMachine, VMHost, DataStore


import csv
dataReader = csv.reader(open(csv_filepathname))

for row in dataReader:
  if  not (row[0].startswith('#') or (row[0] == "Name")):
    # Seek out the vm
    if not VirtualMachine.objects.filter(name=row[0]):
        # Populate the boolean value for the power state
        if row[1].endswith('Off'):
            row[1] = False

        # Only proceed if the virtual host exists
        if VMHost.objects.filter(name = row[5]):
            vm            = VirtualMachine()
            vm.name       = row[0]
            vm.powerState = row[1]
            vm.cpuCount   = row[2]
            vm.memoryMB   = row[3]
            vm.notes      = row[4]
            vm.host       = VMHost.objects.get(name = row[5])
            vm.save()
			
			# Seek out the data store, this eliminates blanks
            for d in row[6].split(' '):
                ds  = DataStore.objects.get(name = d)
                vm.datastore.add(ds)
                print '  added datastore ({0})'.format(d)

            print 'Virtual Machine ({0}) created'.format(row[0])

        else:
            print 'Virtual host({0}) does not exist'.format(row[5])
    else:
        print 'Virtual machine ({0}) already exists'.format(row[0])
        vm = VirtualMachine.objects.get(name=row[0])
    vm.save()