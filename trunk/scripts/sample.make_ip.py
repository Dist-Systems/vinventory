import sys,os,csv

# Full path to your django project directory
path = os.path.abspath('.')

# Full path and name to your csv file
csv_filepathname=path+"/data/IpAddress.csv"

sys.path.append(path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from inventory.models import VirtualMachine, IpAddress


import csv
dataReader = csv.reader(open(csv_filepathname))

# For every line in the file (lines represent virtual machines)
for row in dataReader:

  # Does the line have data?
  if  not (row[0] == "Name"):
    # Does this virtual machine have an associated IP?
    if row[1] != '':
      vm_exists = VirtualMachine.objects.filter(name=row[0])
      if(vm_exists):
        vm = VirtualMachine.objects.get(name=row[0])
        # For each IP address...
        for i in row[1].split(' '):
          print i,
          ip_exists = IpAddress.objects.filter(address=i)
          if not(ip_exists):
            ip         = IpAddress()
            print ' ...created'
          else:
            ip  = IpAddress.objects.get(address=i)
            print ' ...exists', 
          ip.address = i
          ip.vm      = vm
          ip.save()
          print 'and updated'
      else:
        print 'Virtual Machine {0} doesn\'t exist!'.format(row[0])
