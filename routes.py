# Import the built-in libraries
import os

# Import external libraries
import numpy as np
import pandas as pd
import pickle
from flask import Blueprint, request
import json

# Import customized libraries
from src.utils.helpers import DIR_DATA_BGP
from src.utils.geolocator import geolocator

my_routes = Blueprint('my_routes', __name__)

# Pre-load all the needed data
outage_summary: dict = pickle.load(open(os.path.join(DIR_DATA_BGP, 'outage_summary.pkl'), 'rb'))
update_features: pd.DataFrame = pickle.load(open(os.path.join(DIR_DATA_BGP, 'update_features.pkl'), 'rb'))

# Summary of the outage, return in json format
# TODO: implement this function with more details
@my_routes.route('/summary', methods=['GET'])
def summary():
    response = {}
    for prefix, timestamps in outage_summary.items():
        ip = prefix.split('/')[0]
        geolocation = geolocator.geolocate_ip(ip)
        response[prefix] = {
            'cc': geolocation if geolocation else 'Unknown',
            'timestamps': timestamps
        }
    # parse the dataframe to json format
    return json.dumps(response)

# Detail information of one specific prefix, return in json format
# TODO: implement this function with more details
@my_routes.route('/detail/prefix', methods=['GET'])
def detail_prefix():
    # get the parameters from the request
    try:
        prefix = request.args['prefix']
    except KeyError:
        return json.dumps({'error': 'No prefix provided!'})
    response = {}
    # find related features of the given prefix
    features = update_features[update_features['prefix'] == prefix]
    if features.empty:
        return json.dumps({'error': 'No such prefix found!'})
    for index, row in features.iterrows():
        response[row['time']] = {
            'num_announce': row['num_announce'],
            'num_withdraw': row['num_withdraw']
        }
    return json.dumps(response)

# Detail information of one specific ASN, return in json format
# TODO: implement this function referring to the other two functions
@my_routes.route('/detail/asn', methods=['GET'])
def detail_asn():
    return json.dumps({'error': 'Not implemented yet!'})

# TODO: You need to implement extra functions for AS Topology or Real-Time BGP data feed.
# You should add more routes here!