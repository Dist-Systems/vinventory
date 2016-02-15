vinventory
==========

Django based project to keep track of network (distributed systems) inventory.
The need arose to develop a better way to keep track of our distributed systems inventory. Both physical and virtual. This is a little django project that accomplished the task.

(originally posted on https://code.google.com/p/vinventory/ in 2011)


Get an inventory system that can work with our distributed systems (including vsphere inventory and offline systems). Preferred option is to meet the following requirements:

- Utilize as many existing resources as possible: doing so will take advantage of existing documentation, online resources, user groups and bugfixes.
- Have (at least) the functionality of the (now outdated) sysinfo system

The designed solution currently utilizes several popular components which form an aggregate system that will likely fit our needs. The utilized components are:

- windows PowerShell (required to be installed in order to usePwerCLI)
- VMware vSphere PowerCLI 4.1.1 (vmware tool, used to access the API)
- Lighttpd (efficient & event-driven light webserver that is simple to configure)
- Django (web framework to manage the data and present an interface to it)
- HTML5Boilerplate (template for the html/css presentation)


cp settings.py.sample settings.py
sudo easy_install pagination
