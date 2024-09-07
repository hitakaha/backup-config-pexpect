# Sample script to backup config
## Prerequisite:
### Python
```
pip install pexpect
```

### TFTP server
```
apt install tftpd-hpa
```

Then, change /etc/default/tftpd-hpa

[From] TFTP_OPTIONS="--secure"

[To] TFTP_OPTIONS="--secure --create"

```
sudo service tftpd-hpa restart
```

Change owner of the directory to tftp

```
sudo chown -R tftp /srv/tftp
```

## How to use
Configure IP address of TFTP server and Prompt.

```
TFTP_SERVER = "172.30.0.1"
PROMPT = "RP/0/RP0/CPU0"
```

Configure tareget host info.
"hostname": ["IP addresss", "username", "password"]

```
hosts={
    "xrd-1": ["172.30.0.2", "admin", "admin"],
    "xrd-2": ["172.30.0.3", "admin", "admin"]
}
```


## Outputs
```
# python3 backup_pexpect.py
=== Start ===
Backup config host: xrd-1
Login info: ssh -o StrictHostKeyChecking=no admin@172.30.0.2
send command: copy run tftp://172.30.0.1/xrd-1.cfg
=== Done ===
=== Start ===
Backup config host: xrd-2
Login info: ssh -o StrictHostKeyChecking=no admin@172.30.0.3
send command: copy run tftp://172.30.0.1/xrd-2.cfg
=== Done ===
```
