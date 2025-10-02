# scapy-doo

## Install

1. `python3 -m venv .venv`
2. `source .venv/bin/activate`
3. `pip install -r requirements.txt`


## What can we do:
- `packet_reader.py` -> read a packet file, disect packets within, build our own packets ✅
- `port_scan.py` -> scan a list of ports, check for open ports + print results ✅
- `dns_exploration.py` -> scan & discover domains & ips using dns request + reverse dns requests ✅
- `check_default_credentials.py` -> brute force logins using a predefined list of username + password combos against ssh & telnet servers running on localhost ✅
- use `pyinstaller` to package malicious python scripts as executables, targeting the Autorun feature of older Windows versions ✅


## Data sources

- Wireshark sample packets: https://wiki.wireshark.org/samplecaptures#sample-captures

## Tools used

- [Orbstack](https://orbstack.dev/): whip up lightweight virtual Linux machines to test out scripts or run ssh connections