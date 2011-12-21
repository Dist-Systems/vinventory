import sys,os,csv

# Full path to your django project directory
path = os.path.abspath('.')

# Full path and name to your csv file
csv_filepathname=path+"/data/DataStore.csv"

sys.path.append(path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from inventory.models import DataStore

# Define our field names, since the file doesn't match our model
# http://docs.python.org/library/csv.html#csv.DictReader
# http://www.doughellmann.com/PyMOTW/csv/
names = ('name', 'capacityMB', 'freespaceMB', 'filesystemVersion')
dataReader = csv.DictReader(open(csv_filepathname),fieldnames=names)

# Don't need the header, because the names don't match
dataReader.next()

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