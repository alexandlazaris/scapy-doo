from scapy.all import *

packet = rdpcap('http.cap')
print (packet)
# packet with no data
first = packet[0]
# first.show()
# packet with data
data_packet = packet[3]
data_packet.show()
# Raw data contained within TCP packet
# carry http packet, seeing web url, HTTP method type, user agent data, etc
data_packet[TCP].dport = 8080
data_packet.show()
data_packet[TCP].dport = 8045
data_packet.show()

p = IP()/TCP()
p.show()

# can scapy be used to send custom packets?

