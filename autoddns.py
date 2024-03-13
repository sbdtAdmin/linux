#!/data/data/com.termux/files/usr/bin/python

import subprocess, os, datetime, threading, time

def get_ip():
    import re, subprocess
    found_ips = []
    
    found = False
    while not found:
        text = subprocess.run("ifconfig".split(" "), capture_output=True, text=True).stdout
        
        # Регулярное выражение для поиска IP-адресов
        ip_regex = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
        
        # Поиск всех соответствий в тексте
        found_ips = re.findall(ip_regex, text)
        if len(found_ips) in [0, 1]:
            print("Connecting...")
        else: 
            found = True
        time.sleep(1)
    
    
    return found_ips[2]

def set_ddns(HOSTNAME, IP_ADDRESS, USERNAME, PASSWORD):
    url_address = f"http://dynupdate.no-ip.com/nic/update?hostname={HOSTNAME}&myip={IP_ADDRESS}"
    
    print()
    print(str(datetime.datetime.now()).split(".")[0])
    os.system(f'curl "{url_address}" -u {USERNAME}:{PASSWORD}')
        
        
HOSTNAME = "illya.ddns.net"
USERNAME = "ispining"
PASSWORD = "52545658lL"
        
while True:
    
    IP_ADDRESS = get_ip()
    
    set_ddns(HOSTNAME, IP_ADDRESS, USERNAME, PASSWORD)

    time.sleep(2*60)

