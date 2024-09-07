#!/usr/bin/env python3
"""
Simple script to backup configs

Prerequisits:
- Python:
  pip install pexpect

- TFTP server
  apt install tftpd-hpa

"""

from logging import DEBUG, INFO
import logging
import pexpect

# Please configure following
TFTP_SERVER = "172.30.0.1"
PROMPT = "RP/0/RP0/CPU0"

# Enable/disable debug outputs
LOG_LEVEL = "INFO"
#LOG_LEVEL = "DEBUG"


# Define access info for target devices
# Format:
#   "hostname": ["address", "username", "password"]
hosts={
    "xrd-1": ["172.30.0.2", "admin", "cisco123"],
    "xrd-2": ["172.30.0.3", "admin", "cisco123"],
    "xrd-3": ["172.30.0.4", "admin", "cisco123"],
    "xrd-4": ["172.30.0.5", "admin", "cisco123"],
    "xrd-5": ["172.30.0.6", "admin", "cisco123"],
    "xrd-6": ["172.30.0.7", "admin", "cisco123"],
    "xrd-7": ["172.30.0.8", "admin", "cisco123"],
    "xrd-8": ["172.30.0.9", "admin", "cisco123"]
}


def set_logger():
    """
    Set logger
    """

    logger = logging.getLogger("logname")
    stream = logging.StreamHandler()
    logger.addHandler(stream)

    logger.setLevel(LOG_LEVEL)

    return logger


def main():
    """
    main function
    """

    log = set_logger()

    for host,params in hosts.items():
        print("=== Start ===")
        print("Backup config host: "+str(host))
        log.debug(f"host = {params[0]}")
        log.debug(f"host = {params[1]}")
        log.debug(f"host = {params[2]}")

        login = "ssh -o StrictHostKeyChecking=no "+params[1]+"@"+params[0]
        print("Login info: "+str(login))
        r = pexpect.spawn(login)

        log.debug(r.before)
        log.debug(r.after)
        log.debug(r.buffer)
        r.expect("Password")
        r.sendline(params[2])

        log.debug(r.before)
        log.debug(r.after)
        log.debug(r.buffer)
        r.expect(PROMPT)
        command="copy run tftp://"+TFTP_SERVER+"/"+host+".cfg"
        print("send command: "+str(command))
        r.sendline(command)

#        log.debug(r.before)
#        log.debug(r.after)
#        log.debug(r.buffer)
#        r.expect("Host name or IP address")
#        r.sendline("\n")
#
        log.debug(r.before)
        log.debug(r.after)
        log.debug(r.buffer)
        r.expect("Destination file name")
        r.sendline("\n")

        log.debug(r.before)
        log.debug(r.after)
        log.debug(r.buffer)
        r.expect(PROMPT)
        r.sendline("exit")
        print("=== Done ===")

if __name__ == "__main__":
    main()
