import sys,os

# Full path to your django directory
path = os.path.abspath('.')

sys.path.append(path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from inventory.utils import createDataStores, createVirtualHosts, createVirtualMachines, createIPs, clearAll 

def ds():
  datastore_file  = path+"/data/DataStore.csv"
  datastore_names = ('name', 'capacityMB', 'freespaceMB', 'filesystemVersion')
  createDataStores(datastore_file, datastore_names)

def vmh():
  vmhost_file  = path+'/data/VMHost.csv'
  vmhost_names = ('Name','Manufacturer','Model','NumCpu','CpuTotalMhz','CpuUsageMhz','ProcessorType')
  createVirtualHosts(vmhost_file, vmhost_names)

def vm():
  vm_file  = path+'/data/VirtualMachine.csv'
  vm_names = ('Name','PowerState','NumCpu','MemoryMB','Notes','VMHost','Datastore')
  createVirtualMachines(vm_file, vm_names)

def ip():
  ip_file  = path+"/data/IpAddress.csv"
  ip_names =  ('vm','ip')
  createIPs(ip_file, ip_names)

if __name__ == '__main__':
  clearAll()
  ds()
  vmh()
  vm()
  ip()