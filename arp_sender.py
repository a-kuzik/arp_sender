from scapy.all import *
from netaddr import *


class ArpSend:
    def __init__(self):
        pass

    def split_net(self, net, split_mask, max_prfxs=None):
        subnets = []
        num_total = 0
        ip = IPNetwork(net)
        if max_prfxs == None:
            for subnet in list(ip.subnet(split_mask)):
                subnets.append(str(subnet))
        elif max_prfxs != None:
            for subnet in list(ip.subnet(split_mask)):
                num_total += str(subnet).count("/")
                subnets.append(str(subnet))
                if num_total == max_prfxs:
                    break
        return subnets

    def arp_request(self, src_mac, src_ip, dst_ip, iface, vlan=None):
        dst = "ff:ff:ff:ff:ff:ff"
        if vlan != None:
            pkt = (
                Ether(dst=dst)
                / Dot1Q(vlan=vlan)
                / ARP(op="who-has", psrc=src_ip, pdst=dst_ip, hwsrc=src_mac)
            )
        else:
            pkt = Ether(dst=dst) / ARP(
                op="who-has", psrc=src_ip, pdst=dst_ip, hwsrc=src_mac
            )
        sendp(pkt, iface=iface)


arp = ArpSend()
net = "172.16.142.200/28"
split_mask = 32
ips = arp.split_net(net, split_mask)
src_mac = "0c:de:80:12:90:01"
iface = "vlan.1955"
dst_ip = "172.16.142.2"

for ip in ips:
    arp.arp_request(src_mac, ip, dst_ip, iface)
