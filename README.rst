libvirt-inventory
=================

Description
***********
Dynamic inventory for ansible, that return running vms

Installation/Usage
******************
- $ yay -S python-libvirt
- $ ./setup.py install --user
- $ libvirt-inventory --list

{'all': {'hosts': ['192.168.100.5', '192.168.100.4', '192.168.100.6'], 'vars': {}}, '_meta': {'hostvars': {}}}
