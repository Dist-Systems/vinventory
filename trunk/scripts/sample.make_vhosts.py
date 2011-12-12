#change these variables to suit your environment
username = 'user'

# Full path and name to your csv file
csv_filepathname="/Users/{0}/Desktop/vinventory/data/VMHost.csv".format(username)

# Full path to your django project directory
your_djangoproject_home="/Users/{0}/Desktop/vinventory/".format(username)


import sys,os
sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from inventory.models import VMHost, Vendor


import csv
dataReader = csv.reader(open(csv_filepathname))
Vendors = Vendor.objects.filter()
for row in dataReader:
  if  not (row[0].startswith('#') or (row[0] == "Name")):
    print row[1],
    v_exists = Vendor.objects.filter(name=row[1])
    if not(v_exists):
        # create vendor
        v  =  Vendor()
        v.name = row[1]
        v.save()
        print ' ...created'
    else:
        v  = Vendor.objects.get(name=row[1])
        print ' ...exists'

    print row[0],
    vmh_exists = VMHost.objects.filter(name=row[0])
    if not(vmh_exists):
        vmh              = VMHost()
        vmh.name         = row[0]
        vmh.manufacturer = v
        vmh.model        = row[2]
        vmh.cpuCount     = row[3]
        vmh.cpuTotal     = row[4]
        vmh.cpuUsage     = row[5]
        vmh.processor    = row[6]
        vmh.save()
        print ' ...created'
    else:
        print ' ...exists'
