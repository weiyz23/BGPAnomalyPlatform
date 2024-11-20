# Import the built-in libraries
import os
import sys
import time

# Import external libraries
import numpy as np
import pandas as pd

# Import customized libraries
from config import flask_config, flask_folder
from src.utils.geolocator import geolocator

# class for BGP Anomaly Detection
# This basic class only detect the outages from the BGP Update Data
# You can extend this class to detect the outages from the BGP RIB Data
class DefaultDetector:
    
    def __init__(self):
        pass 
        
    # Singleton pattern
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DefaultDetector, cls).__new__(cls)
        return cls.instance
        
    
    # Extract the features from the BGP Update Data
    # TODO: You need to implement a good algorithm, instead of this baseline algorithm
    def detect(self, _input_feature: pd.DataFrame):
        print("Calculating statistics from the BGP Update Features")
        # iterate over the dataframe, get the statistics for each prefix
        dict_prefix_statistics = {}
        
        count = 0
        
        # calculate the standard deviation for each prefix of the hourly announce and withdraw
        for index, row in _input_feature.iterrows():
            prefix = row['prefix']
            timestamp = row['time']
            if prefix not in dict_prefix_statistics:
                dict_prefix_statistics[prefix] = [[], [], []]
                # just add them to the list
            dict_prefix_statistics[prefix][0].append(row['num_announce'])
            dict_prefix_statistics[prefix][1].append(row['num_withdraw'])
            dict_prefix_statistics[prefix][2].append(timestamp)
            count += 1
            if count % 100000 == 0:
                print(f"Processed {count} records")
        
        print("Detecting the Outages from the BGP Update Data")
        # calculate the standard deviation for each prefix
        dict_prefix_outages = {}
        for prefix, values in dict_prefix_statistics.items():
            # if their are all zeros, then we simply ignore them
            if np.sum(values[0]) == 0 or np.sum(values[1]) == 0:
                continue
            std_announce = np.std(values[0], where=np.array(values[0]) > 0)
            std_withdraw = np.std(values[1], where=np.array(values[1]) > 0)
            mean_announce = np.mean(values[0], where=np.array(values[0]) > 0)
            mean_withdraw = np.mean(values[1], where=np.array(values[1]) > 0)
            # check each time slice, if the num > avg + 5 * std, then we simply consider it is an outage
            for idx, (num_announce, num_withdraw, timestamp) in enumerate(zip(values[0], values[1], values[2])):
                if num_announce > mean_announce + 3 * std_announce or num_withdraw > mean_withdraw + 3 * std_withdraw:
                    if prefix not in dict_prefix_outages:
                        dict_prefix_outages[prefix] = []
                    # add the outage time
                    dict_prefix_outages[prefix].append(timestamp)
        return dict_prefix_outages