from scapy.all import *

# popular ports with web servers, sql, dns, etc
ports = [25, 80, 53, 443, 445, 8080, 8443]

# "S" = syn flag
def syn_scan(host):
    ans, unans = sr(IP(dst=host)/TCP(sport=5555, dport=ports, flags="S"), timeout=2, verbose=0)
    print("Open ports at %s:" % host)
    for (s, r,) in ans:
        if s[TCP].dport == r[TCP].sport:
            print(f"-> {s[TCP].dport}")
    print ("closed ports:")
    for u in unans:
        print (f"-x {u[TCP].dport}")

host = "8.8.8.8"
syn_scan(host)
