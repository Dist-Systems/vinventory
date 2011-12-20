import sys,os,csv

# Full path to your django project directory
path = os.path.abspath('.')

# Full path and name to your csv file
csv_filepathname=path+"/data/VirtualMachine.csv"

sys.path.append(path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from inventory.models import VirtualMachine, VMHost, DataStore


import csv
dataReader = csv.reader(open(csv_filepathname))

for row in dataReader:
  if  not (row[0] == "Name"):

    # Seek out the vm
    if not VirtualMachine.objects.filter(name=row[0]):
        # If the VM doesn't exist, we create it

        # Only proceed if the virtual host exists
        if VMHost.objects.filter(name = row[5]):
            # Create a new virtual machine
            vm = VirtualMachine()
            vm.name       = row[0]
        else:
            msg = 'Virtual host({0}) does not exist'.format(row[5])
            # http://docs.python.org/tutorial/errors.html
            raise RuntimeError(msg)

        # Populate the boolean value for the power state (any sting is True)
        if row[1].endswith('Off'):
            row[1] = False
        vm.powerState = row[1]
        vm.cpuCount   = row[2]
        vm.memoryMB   = row[3]
        vm.host       = VMHost.objects.get(name = row[5])
        vm.save()
        print '({0}) created'.format(row[0]),

    else:
        # The vitual machine exists, assign it to 'vm'
        print '({0}) already exists'.format(row[0]),
        vm = VirtualMachine.objects.get(name=row[0])

    # The following is performed on existing or newly created VMs
    # Seek out the data store, this eliminates blanks
    for d in row[6].split(' '):
        ds  = DataStore.objects.get(name = d)
        vm.datastore.add(ds)
        print '  added datastore ({0})'.format(d)
   
    # Name is the identifier, so we can't update it
    # vm.name       = row[0]
    vm.powerState = row[1]
    vm.cpuCount   = row[2]
    vm.memoryMB   = row[3]
    vm.notes      = row[4]
    vm.host       = VMHost.objects.get(name = row[5])
    vm.save()
    print 'updated'