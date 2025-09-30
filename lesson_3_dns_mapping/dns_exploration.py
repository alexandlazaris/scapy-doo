import dns
import dns.resolver
import socket

def reverse_dns(ip):
    """
    Find publically accessibly domains associated with the given ip.

    Example, given this result:
    ('syd09s31-in-f14.1e100.net', ['78.221.251.142.in-addr.arpa'], ['142.251.221.78'])
    
    [0] - primary domain name (aka the canonical name) associated with the given ip.
    
    [1] - not the ip address of the domain, but a formatted version of the server ip that allows DNS servers to look up the corresponding domain name. This ip address is the provided ip addres revered & appended with `.in-addr.arpa`. Used by servers to match a domain name for a given ip address.
    
    [2] - is the ip address provided into the reverse dns lookup, ensuring the result corresponds to the correct ip.
    """
    try:    
        result = socket.gethostbyaddr(ip)
    except:
        return []
    return [result[0]] + result[1] + result[2]

def dns_request(domain):
    """
    Resolves a dns request, when providing a base domain, returning discovered ips. 
    """
    try:
        result = dns.resolver.resolve(domain, 'A')
        if result:
            print (f"number of ips at \"{domain}\": {len(result)}")
            for ip in result:
                list_results = reverse_dns(ip.to_text())
                print (f"subdomain \"{domain}\" with ip {ip}: \n-> primary domain name: {list_results[0]}\n-> reverse lookup domain name: {list_results[1]}\n-> provided ip: {list_results[2]}")
    except (dns.resolver.NXDOMAIN, dns.exception.Timeout):
        return

def sub_domain_search(domain_name, dictionary, nums):
    """
    Subdomains often contain numbers appended (e.g mail1, www4, etc) to indicate named servers of those subdomains.

    For each subdomain, run the dns + reverse dns functions. 

    If `nums=True, loops through each subdomain suffix (from 0-10), running a reverse dns lookup against each discovered subdomain ip.
    """
    for sub in dictionary:
        subdomain_name = f"{sub}.{domain_name}"
        print (f"prefixing \"{sub}\" into domain \"{domain_name}\"")
        print (f"new subdomain is: \"{subdomain_name}\"")
        dns_request(subdomain_name)
        if nums:
            for i in range(0, 10):
                sub_prefix = f"{sub}{str(i)}"
                subdomain_name = f"{sub_prefix}.{domain_name}"
                s = f"{sub}{str(i)}.{domain_name}"
                dns_request(s)

# the target base domain
domain = "google.com"
# a list of common subdomains
d = "subdomains.txt"
dictionary = []
with open(d, "r") as f:
    dictionary = f.read().splitlines()
# search for a list of subdomains against a base domain, printing the subdomain ip & 
sub_domain_search(domain, dictionary, True)