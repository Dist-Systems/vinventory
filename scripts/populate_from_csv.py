import sys,os
# Full path to your current directory
path = os.path.abspath('.')

sys.path.append(path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from inventory.utils import *

# file paths & column names
datastore_file  = path+"/data/DataStore.csv"
datastore_names = ('name', 'capacityMB', 'freespaceMB', 'filesystemVersion')
d = openDataSource(datastore_file, datastore_names)
createDataStores(d)

vmhost_file  = path+'/data/VMHost.csv'
vmhost_names = ('Name','Manufacturer','Model','NumCpu','CpuTotalMhz','CpuUsageMhz','ProcessorType')
d = openDataSource(vmhost_file, vmhost_names)
createVirtualHosts(d)

vm_file  = path+'/data/VirtualMachine.csv'
vm_names = ('Name','PowerState','NumCpu','MemoryMB','Notes','VMHost','Datastore')
d = openDataSource(vm_file, vm_names)
createVirtualMachines(d)

ip_file  = path+"/data/IpAddress.csv"
ip_names =  ('vm','ip')
d = openDataSource(ip_file, ip_names)
createIPs(d)