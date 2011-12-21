import sys,os,csv

# Full path to your django project directory
path = os.path.abspath('.')

# Full path and name to your csv file
csv_filepathname=path+"/data/VMHost.csv"

sys.path.append(path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from inventory.models import VMHost, Vendor

import csv
dataReader = csv.reader(open(csv_filepathname))
Vendors = Vendor.objects.filter()
for row in dataReader:
  if  not (row[0].startswith('#') or (row[0] == "Name")):
    print row[1],
    if not Vendor.objects.filter(name=row[1]):
        # create vendor
        v  =  Vendor()
        v.name = row[1]
        v.save()
        print ' ...created'
    else:
        v  = Vendor.objects.get(name=row[1])
        print ' ...exists'

    print row[0],

    if not VMHost.objects.filter(name=row[0]):
        vmh      = VMHost()
        vmh.name = row[0]
        print ' ...created'
    else:
        vmh = VMHost.objects.get(name=row[0])
        print ' ...exists'
    
    vmh.manufacturer = v
    vmh.model        = row[2]
    vmh.cpuCount     = int(row[3])
    vmh.cpuTotal     = int(row[4])
    vmh.cpuUsage     = row[5]
    vmh.processor    = row[6]
    vmh.save()
print 'updated'
