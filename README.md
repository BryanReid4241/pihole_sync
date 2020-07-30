PiHole Sync
-----

Sync your custom dns entries between multiple pihole servers, as well as keeping it in code

Install
---
*Requires python3*

```
pip3 install -r requirements.txt
```

Usage
----

```
python pihole_sync.py --username root --password $PASSWORD --config config.yml --hosts-file hostsfile

```