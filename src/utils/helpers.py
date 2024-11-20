# ==============================================
# Utils functions
# ==============================================

# Import the built-in libraries
import os
import subprocess
import time
import datetime

# Absolute path of the data directory
DIR_DATA_GEOLOCATION = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../../data/geolocation")
DIR_DATA_BGP = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../../data/bgp")

def ip_to_int(ip):
    ip = list(map(int, ip.split('.')))
    return ip[0] * 256 ** 3 + ip[1] * 256 ** 2 + ip[2] * 256 + ip[3]

def int_to_ip(ip_int):
    return '.'.join([str(ip_int // 256 ** i % 256) for i in range(3, -1, -1)])

# if the range provided is not a CIDR block, then divide the range into smaller blocks
# and return a list of the starting ip of blocks
# eg: 0.0.0.1-0.0.0.3 should be divided into 0.0.0.1/32 and 0.0.0.2/31, while 0.0.0.2-0.0.0.6 should be divided into 0.0.0.2/31, 0.0.0.4/31 and 0.0.0.6/32
def divide_into_blocks(ip_start, ip_end):
    ip_start_int = ip_to_int(ip_start)
    ip_end_int = ip_to_int(ip_end)
    blocks = []
    while ip_start_int <= ip_end_int:
        mask = 0
        # get the non-1 suffix length
        suffix_len = 0
        while (ip_start_int >> suffix_len) & 1 == 0:
            suffix_len += 1
        # check if all 1 suffixes can be in the range
        mask = 0xffffffff >> (32 - suffix_len)
        while (ip_start_int | mask) > ip_end_int:
            mask >>= 1
        # the block is too large, split it and check the remaining range
        blocks.append(ip_start_int)
        ip_start_int = (ip_start_int | mask) + 1
    return blocks


def subprocess_cmd(command):
    output = subprocess.check_output(command, shell=True).decode('utf-8')
    print(output)