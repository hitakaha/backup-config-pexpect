#!/usr/bin/env python3
"""
Simple script to backup configs

Prerequisits:
  pip install pexpect
"""

from logging import DEBUG, INFO
import logging
import pexpect

# Please configure following
TFTP_SERVER = "192.168.4.2"
PROMPT = "RP/0/RP0/CPU0"

# Enable/disable debug outputs
#LOG_LEVEL = "INFO"
LOG_LEVEL = "DEBUG"


# Define access info for target devices
# Format:
#   "hostname": ["address", "username", "password"]
hosts={
    "xr9kv1": ["192.168.4.111", "cisco", "cisco"],
    "xr9kv2": ["192.168.4.112", "cisco", "cisco"],
    "xr9kv3": ["192.168.4.113", "cisco", "cisco"],
    "xr9kv4": ["192.168.4.114", "cisco", "cisco"],
    "xr9kv5": ["192.168.4.115", "cisco", "cisco"],
    "xr9kv6": ["192.168.4.116", "cisco", "cisco"],
    "xr9kv7": ["192.168.4.117", "cisco", "cisco"]
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
    log.debug("debug")
    log.info("info")

    for host,params in hosts.items():
        print("=== Start ===")
        print("Backup config host="+str(host))
        log.debug(f"host = {params[0]}")
        log.debug(f"host = {params[1]}")
        log.debug(f"host = {params[2]}")

        login = "ssh "+params[1]+"@"+params[0]
        print("Login info="+str(login))
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
        print("send command"+str(command))
        r.sendline(command)

        log.debug(r.before)
        log.debug(r.after)
        log.debug(r.buffer)
        r.expect("Host name or IP address")
        r.sendline("\n")

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
