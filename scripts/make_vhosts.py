import sys,os,csv

# Full path to your django project directory
path = os.path.abspath('.')

# Full path and name to your csv file
csv_filepathname=path+'/data/VMHost.csv'

sys.path.append(path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from inventory.models import VMHost, Vendor

# Define our field names, since the file doesn't match our model
names = ('Name','Manufacturer','Model','NumCpu','CpuTotalMhz','CpuUsageMhz','ProcessorType')
dataReader = csv.DictReader(open(csv_filepathname), fieldnames=names)

# Don't need the header, because the names don't match
dataReader.next()

# For every line in the file (lines represent Virtual Machine Hosts)
for row in dataReader:
    print row['Manufacturer'],
    
    # Seek an existing vendor (since vendor is a requirement)
    if not Vendor.objects.filter(name=row['Manufacturer']):
        # create vendor
        v  =  Vendor()
        v.name = row['Manufacturer']
        v.save()
        print ' ...created'
    else:
        v  = Vendor.objects.get(name=row['Manufacturer'])
        print ' ...exists'
    
    print row['Name'],
    
    # Seek out an existing Virtual Machine Host
    if not VMHost.objects.filter(name=row['Name']):
        # If it does not exist, create one and specify the name
        vmh      = VMHost()
        vmh.name = row['Name']
        print ' ...created'
    else:
        # If it exists, grab it and assign it to vmh variable
        vmh = VMHost.objects.get(name=row['Name'])
        print ' ...exists'

    # We can now update the object and save it
    vmh.manufacturer = v
    vmh.model        = row['Model']
    vmh.cpuCount     = int(row['NumCpu'])
    vmh.cpuTotal     = int(row['CpuTotalMhz'])
    vmh.cpuUsage     = row['CpuUsageMhz']
    vmh.processor    = row['ProcessorType']
    vmh.save()
print 'updated'
