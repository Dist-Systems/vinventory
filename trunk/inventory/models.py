from django.db import models
from django.forms import ModelForm

# Abstract class that other inventory items can inherit from
# http://stackoverflow.com/questions/1737017/django-auto-now-and-auto-now-add
class ISCNode(models.Model): 
    ROLE_CHOICES = (
        (u'dev',  u'Development'),
        (u'prod', u'Production'),
    )
    name       = models.CharField(max_length="30",unique=True, editable=False)
    notes      = models.TextField(blank=True)
    role       = models.CharField(max_length=4, choices=ROLE_CHOICES, blank=True)
    
	# These fields are hidden from the administrative interface
    created    = models.DateTimeField(auto_now_add=True)
    modified   = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
      return ('system-display', (), {'object_id': self.id})

    class Meta:
        abstract = True	

# Child class of ISCNode for 'on-the-iron' servers
class Server(ISCNode):
    vender     = models.ForeignKey('Vendor')
    capacityMB = models.IntegerField()
    cpuCount   = models.PositiveSmallIntegerField()
    purchased  = models.DateTimeField(blank=True)

# Datastores can hold many VMHosts, by making 
# a separate class, we avoid typos
class DataStore(ISCNode):
    capacityMB           = models.IntegerField()
    freespaceMB          = models.IntegerField()
    filesystemVersion    = models.DecimalField(max_digits=3, decimal_places=2)


# VMHost can hold many VirtualMachines, by making 
# a separate class, we avoid typos
class VMHost(ISCNode):
    manufacturer = models.ForeignKey('Vendor')
    model        = models.CharField(max_length="30")
    cpuCount     = models.PositiveSmallIntegerField(editable=False)
    cpuTotal     = models.PositiveSmallIntegerField(editable=False)
    cpuUsage     = models.PositiveSmallIntegerField(editable=False)
    processor    = models.CharField(max_length="50")


# Child class of ISCNode
class VirtualMachine(ISCNode):
    powerState = models.NullBooleanField()
    cpuCount   = models.IntegerField()
    memoryMB   = models.IntegerField()
    host       = models.ForeignKey('VMHost')
    datastore  = models.ForeignKey('DataStore')

# A class for Vendors, to avoid duplication
# or typos by manual entry
class Vendor(models.Model):
    name         = models.CharField(max_length="30")
    website      = models.CharField(max_length="100", blank=True)

    def __unicode__(self):
        return self.name

# IP addresses might not need their own class, but this 
# was a design consideration that would be another safeguard
# against assigning an IP that is already in use and to avoid typos
class IpAddress(models.Model):
    address = models.IPAddressField(unique=True)
    vm      = models.ForeignKey(VirtualMachine)

    def __unicode__(self):
        return self.address