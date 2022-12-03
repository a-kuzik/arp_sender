# arp_sender

This is a small and simple script for testing network equipment.

Before starting it, you need to change the values of the variables in the arp_sender.py script.

The variable **net** controls the number of generated ARPs. It should be part of the direct network and be less specific. 

The **split_mask** variable must not be changed.

The **src_mac** variable is the MAC address of the interface ARP source (depending on the OS, it is determined by the ifconfig or ipconfig command).

The **iface** variable is the name of the interface of ARP source.

The variable **dst_ip** is the point-to-point address of the network node interface where ARP requests will be sent.

If the link between the ARP source and the testing node under test is tagged, then you must specify the vlan-id value for the **vlan** variable.

Running the script:

*python3 sender.py*

Result:
```
A:LAB# show router arp 

===============================================================================
ARP Table (Router: Base)
===============================================================================
IP Address      MAC Address       Expiry    Type   Interface
-------------------------------------------------------------------------------
-----------------------------------------------------------------------------------
172.16.142.192  0c:de:80:12:90:01 01h17m50s Dyn[I] to_upl_srvr1
172.16.142.193  0c:de:80:12:90:01 01h17m50s Dyn[I] to_upl_srvr1
172.16.142.194  0c:de:80:12:90:01 01h17m50s Dyn[I] to_upl_srvr1
172.16.142.195  0c:de:80:12:90:01 01h17m50s Dyn[I] to_upl_srvr1
172.16.142.196  0c:de:80:12:90:01 01h17m50s Dyn[I] to_upl_srvr1
172.16.142.197  0c:de:80:12:90:01 01h17m50s Dyn[I] to_upl_srvr1
172.16.142.198  0c:de:80:12:90:01 01h17m50s Dyn[I] to_upl_srvr1
172.16.142.199  0c:de:80:12:90:01 01h17m50s Dyn[I] to_upl_srvr1
172.16.142.200  0c:de:80:12:90:01 01h17m50s Dyn[I] to_upl_srvr1
172.16.142.201  0c:de:80:12:90:01 01h17m50s Dyn[I] to_upl_srvr1
172.16.142.202  0c:de:80:12:90:01 01h17m50s Dyn[I] to_upl_srvr1
172.16.142.203  0c:de:80:12:90:01 01h17m50s Dyn[I] to_upl_srvr1
172.16.142.204  0c:de:80:12:90:01 01h17m50s Dyn[I] to_upl_srvr1
172.16.142.205  0c:de:80:12:90:01 01h17m50s Dyn[I] to_upl_srvr1
172.16.142.206  0c:de:80:12:90:01 01h17m50s Dyn[I] to_upl_srvr1
172.16.142.207  0c:de:80:12:90:01 01h17m50s Dyn[I] to_upl_srvr1
-------------------------------------------------------------------------------
No. of ARP Entries: 25
===============================================================================
A:LAB#
```
