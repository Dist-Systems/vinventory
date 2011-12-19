import sys,os,csv

# Full path to your django project directory
path = os.path.abspath('.')

# Full path and name to your csv file
csv_filepathname=path+"/data/DataStore.csv"

sys.path.append(path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from inventory.models import DataStore

dataReader = csv.DictReader(open(csv_filepathname))

for row in dataReader:
    print row['name'],
    exists = DataStore.objects.filter(name=row['name'])
    if not exists:
        #"Name","CapacityMB","FreeSpaceMB","FileSystemVersion"
        datastore = DataStore(**row)
        
        print '... created'
    else:
        #print row,"...exists",
        exists.update(**row)
        datastore = DataStore.objects.get(name=row['name'])
        print "...updated"
    datastore.save()