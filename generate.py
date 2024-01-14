import json, requests
from tqdm import tqdm

adlist = json.loads(open('adlist.json', 'r').read())

id = 0
domains = []
for ad in tqdm(adlist):
    address = adlist[id]['address']
    try:
        r = requests.get(address, timeout=10)
        if r.status_code == 200:
            for i in r.text.split('\n'):
                i = i.strip().replace('0.0.0.0 ', '').replace('||', '').replace('^', '').replace('\n', '').replace('127.0.0.1', '')
                if i.startswith('#'):
                    continue
                else:
                    domains.append(i)
        id += 1
    except Exception as e:
        print(f"Failed to fetch {e}")


adblock = open('blocklist.txt', 'w+', encoding='utf-8')
dedupe = list(set(domains))
for domain in tqdm(dedupe):
    adblock.write(f"{domain}\n")
adblock.close()