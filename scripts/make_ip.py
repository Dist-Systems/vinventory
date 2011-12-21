import sys,os,csv

# Full path to your django project directory
path = os.path.abspath('.')

# Full path and name to your csv file
csv_filepathname=path+"/data/IpAddress.csv"

sys.path.append(path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from inventory.models import VirtualMachine, IpAddress

# Define our field names, since the file doesn't match our model
names = ('vm','ip')
dataReader = csv.DictReader(open(csv_filepathname),fieldnames=names)

# For every line in the file (lines represent virtual machines)
for row in dataReader:

  # Does the line have data?
  if  not (row['vm'] == "Name"):
    # Does this virtual machine have an associated IP?
    if row['ip'] != '':
      # Yes, there are IP address entries, proceed to process them
	  # Does the associated virual machine exist?
      if VirtualMachine.objects.filter(name=row['vm']):
        # If the virtual machine exists, get it
        vm = VirtualMachine.objects.get(name=row['vm'])
        
		# What IP addresses are currently associated with this vm? 
		# values_list returns a tuple, where the ip address is the 2nd item: ips[1]
        ips = vm.ipaddress_set.values_list()
		
		#declare an empty set
        existing_ips = set()
		
        # For each existing ip
        for ip in ips:
            # add the value to the set
            existing_ips.add(ip[1])

        # For each IP address in the datafile...
        new_ips = set(row['ip'].split(' '))
		
        # Compare the sets
        # http://docs.python.org/library/stdtypes.html#set
        # http://docs.python.org/tutorial/datastructures.html#sets
        ips_to_remove = existing_ips - new_ips
        ips_to_add    = new_ips - existing_ips
		
		
        # If there are IPs to addfor i in ips_to_add:
        for i in ips_to_add:
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
		  
        # If IP addresses have been removed:
        for i in ips_to_remove:
            print i,
            ip_exists = IpAddress.objects.filter(address=i)
            if ip_exists:
                ip  = IpAddress.objects.get(address=i).delete()
                print '... removed',
            else:
                msg = 'IP adress {0} doesn\'t exist!'.format(i)
                raise RuntimeError(msg)
      else:
        msg = 'Virtual Machine {0} doesn\'t exist!'.format(row[0])
        raise RuntimeError(msg)
