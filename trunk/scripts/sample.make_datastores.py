# Full path and name to your csv file
csv_filepathname="path"
# Full path to your django project directory
your_djangoproject_home="path"

import sys,os
sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from inventory.models import DataStore


import csv
dataReader = csv.DictReader(open(csv_filepathname))

for row in dataReader:
    exists = DataStore.objects.filter(name=row['name'])
    if not exists:
        #"Name","CapacityMB","FreeSpaceMB","FileSystemVersion"
        datastore = DataStore(**row)
        datastore.save()
        print '... created'
    else:
        print "...exists"
