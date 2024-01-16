import re, socket, threading, fileinput, sys
from tqdm import tqdm
from queue import Queue

def is_valid_domain(domain):
    domain_pattern = "^((?!-)[A-Za-z0-9-]{1,63}(?<!-)\\.)*[A-Za-z0-9-]{1,63}\\.[A-Za-z]+$"
    return bool(re.match(domain_pattern, domain))

def is_valid_ip(ip):
    ip_pattern = "^(?:[0-9]{1,3}\\.){3}[0-9]{1,3}$"
    return bool(re.match(ip_pattern, ip))

def can_resolve_domain(domain):
    try:
        socket.gethostbyname(domain)
        return True
    except socket.gaierror:
        return False

def check_domains():
    global valid, not_valid, invalid_domains
    valid, not_valid = 0, 0
    invalid_domains = Queue()
    
    with open('blocklist.txt', 'r') as file:
        lines = file.readlines()

    for line in tqdm(lines, desc="Checking domains", unit="domain"):
        line = line.split('#', 1)[0].strip()
        if line == '':
            continue
        if is_valid_domain(line) or is_valid_ip(line):
            valid += 1
        else:
            not_valid += 1
            invalid_domains.put(line)

def check_invalid_domains(pbar):
    global valid
    global not_valid
    while not invalid_domains.empty():
        domain = invalid_domains.get()
        try:
            if can_resolve_domain(domain):
                valid += 1
                not_valid -= 1
        except:
            pass
        pbar.update()

check_domains()

threads = []
pbar = tqdm(total=invalid_domains.qsize(), desc="Checking invalid domains", unit="domain")
for i in range(20):
    t = threading.Thread(target=check_invalid_domains, args=(pbar,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

pbar.close()

def convert_percentage():
    global valid, not_valid
    total = valid + not_valid
    valid = round((valid / total) * 100, 3)
    not_valid = round((not_valid / total) * 100, 3)
    
    return valid, not_valid

def replace_readme():
    valid, not_valid = convert_percentage()
    badge_valid_url = f"https://img.shields.io/badge/Valid-{valid}%25-green"
    badge_invalid_url = f"https://img.shields.io/badge/Invalid-{not_valid}%25-red"
    lines_to_insert = [f'![VALID_BADGE]({badge_valid_url})\n', f'![INVALID_BADGE]({badge_invalid_url})\n']

    with open('readme.md', 'r') as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        if 'INVALID_BADGE' in line:
            lines[i] = lines_to_insert[1]
        elif 'VALID_BADGE' in line:
            lines[i] = lines_to_insert[0]

    with open('readme.md', 'w') as f:
        f.writelines(lines)

replace_readme()