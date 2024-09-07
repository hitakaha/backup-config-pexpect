# Sample script to backup config
## Prerequisits:
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

