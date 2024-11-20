# ==============================================
# Utils functions for downloading BGP data
# ==============================================

# Import the built-in libraries
import os
import random
import sys
import time

# Import external libraries
import pandas as pd
import pickle

# Import customized libraries
from src.utils.bgpstreamer import *

def random_choose_time_slices(_from: datetime, _until: datetime) -> list:
    # each element in the list is a tuple of the start time and the end time
    time_intervels = [] 
    split_days = []
    if _until - _from > timedelta(days=1):
        # divide the time into smaller pieces
        _from_ = _from
        _until_ = _from + timedelta(days=1)
        split_days.append((_from_, _until_))
        while _until_ < _until:
            _from_ = _until_
            _until_ = min(_until_ + timedelta(days=1), _until)
            split_days.append((_from_, _until_))
    else:
        split_days.append((_from, _until))
    # randomly choose 2*1 hours from each day, if the day is shorter than 2 hours, download the whole day
    for _from_, _until_ in split_days:
        if _until_ - _from_ > timedelta(hours=2):
            # randomly choose 2 single hours
            start_list = random.sample(range(0, 24), 2)
            time_intervels.append((_from_ + timedelta(hours=start_list[0]), _from_ + timedelta(hours=start_list[0] + 1)))
            time_intervels.append((_from_ + timedelta(hours=start_list[1]), _from_ + timedelta(hours=start_list[1] + 1)))
        else:
            time_intervels.append((_from_, _until_))
    return time_intervels

def download_one_slice_update_data(_from: datetime, _until: datetime, _filter: str) -> pd.DataFrame:
    print(f"Downloading the BGP Update Data from {_from} to {_until}")
    stream = get_bgp_historical_update_data(
        _from=_from,
        _until=_until,
        _filter=_filter
    )
    # fields: record_type, type, time, project, collector, router, router_ip, peer_asn, peer_address, prefix, next-hop, as-path
    df_update = pd.DataFrame()
    # set the column type to optimize the memory
    item_list = []
    count = 0
    for elem in stream:
        item = parse_the_bgp_data(elem)
        item_list.append(item)
        count += 1
        if count % 50000 == 0:
            print(f"Downloaded {count} records")
    print(f"Downloaded {count} records")
    df_update = pd.concat([df_update, pd.DataFrame(item_list)], ignore_index=True)
    return df_update


""" CHALLENGE: Currently, we directly download the data to the .bin file, you can use the database to store the data.
To prevent flooding the BGPStream server, we randomly choose 2 hours per day to download the data.
If one day do not longer than 2 hours, we download the data for the whole day.
You can implement the function to download the data to the database for better performance.
"""
def download_historical_update_data(_from: datetime, _until: datetime, _filter: str) -> pd.DataFrame:
    """
    Download the historical BGP Update Data
    :param _from: the start time
    :param _until: the end time
    :param _filter: the filter (You'd better modify the filter, It's very important!)
    :return: the 
    """
    print(f"Downloading the historical BGP Update Data from {_from} to {_until}")

    # Split the time into smaller pieces between _from and _until
    time_slices =  random_choose_time_slices(_from, _until)
    df_update = pd.DataFrame()
    for _from_, _until_ in time_slices:
        df_update = pd.concat([df_update, download_one_slice_update_data(_from_, _until_, _filter)], ignore_index=True)
    return df_update

# Append new data to the existing data in some files
def append_new_data_to_files(file: str, new_data: pd.DataFrame):
    # Remove those duplicated data
    old_data = pickle.load(open(file, 'rb'))
    new_data = pd.concat([old_data, new_data], ignore_index=True)
    # If the timestamp + collector + prefix + next-hop is the same, we consider it as the same record
    new_data = new_data.drop_duplicates(subset=['time', 'type', 'collector', 'prefix', 'next-hop'])
    pickle.dump(new_data, open(file, 'wb'))
    
# TODO: Although there are many helpful functions, maybe you need your own implementation here.