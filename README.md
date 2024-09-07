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

