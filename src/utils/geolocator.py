# ==============================================
# Utils functions for Geolocating IP / ASN / IP Prefix
# You can implement your own logic here
# ==============================================

# Import the built-in libraries
import csv
import os
import sys
from concurrent import futures
from datetime import datetime, timedelta

# Import external libraries
import pybgpstream

# Import customized libraries
sys.path.append('./src')
from src.utils.helpers import *


# Singleton class for geolocation
class Geolocator:
    # build the dataset for geolocation
    def __init__(self):
        self.dict_geolocation = {}
        geolocation_file = os.path.join(DIR_DATA_GEOLOCATION, 'country.csv')
        with open(geolocation_file, 'r') as f:
            for line in f:
                # each line is a leaf node
                ip_start, ip_end, country_code, country_name = line.strip().split(',')[0:4]
                # if is IPv6, ignore
                if '.' not in ip_start:
                    continue
                blocks = divide_into_blocks(ip_start, ip_end)
                for block in blocks:
                    self.dict_geolocation[block] = country_code
    
    # Singleton pattern
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Geolocator, cls).__new__(cls)
        return cls.instance

    # geolocate the single IP
    # CHALLENGE: Implement a better logic
    def geolocate_ip(self, ip):
        subnet_len = 0
        ip_int = ip_to_int(ip)
        while ip_int not in self.dict_geolocation and subnet_len < 32:
            subnet_len += 1
            ip_int >>= subnet_len
            ip_int <<= subnet_len
        if ip_int not in self.dict_geolocation:
            return None
        return self.dict_geolocation[ip_int]

    def geolocate_ip_prefix(self):
        # TODO: Implement Your own logic
        pass
    
    def geolocate_asn(self):
        # TODO: Implement Your own logic
        pass
    
# generate the singleton object
geolocator = Geolocator()

# TODO: Although there are helpful functions, maybe you need your own implementation here.