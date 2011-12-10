# Full path and name to your csv file
csv_filepathname="/Users/elihu/Desktop/vinventory/data/DataStore.csv"
#csv_filepathname="C:\\Users\\ncspa\\Desktop\\vinventory\\data\\DataStore.csv"
# Full path to your django project directory
your_djangoproject_home="/Users/elihu/Desktop/vinventory/"
#your_djangoproject_home='C:\\Users\\ncspa\\Desktop\\vinventory\\'

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
