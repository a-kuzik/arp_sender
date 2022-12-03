# arp_sender

This is a small and simple script for testing network equipment.
Before starting it, you need to change the values of the variables in the arp_sender.py script.
The net variable controls the number of generated ARPs. It should be part of the direct network and be less specific. 
The split_mask variable must not be changed.
The src_mac variable is the MAC address of the interface ARP source (depending on the OS, it is determined by the ifconfig or ipconfig command).
The iface variable is the name of the interface of ARP source.
The variable dst_ip is the point-to-point address of the network node interface where ARP requests will be sent.
If the link between the ARP source and the testing node under test is tagged, then you must specify the vlan-id value for the vlan variable.

Running the script:

python3 sender.py
