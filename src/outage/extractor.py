# Import the built-in libraries
from datetime import timedelta
import os
import sys
import time
import pickle

# Import external libraries
import numpy as np
import pandas as pd

# Import customized libraries
from src.utils.geolocator import geolocator

# Singleton class for feature extraction
# Extract the features from the BGP Data
class FeatureExtractor:
    def __init__(self):
        pass 
        
    # Singleton pattern
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(FeatureExtractor, cls).__new__(cls)
        return cls.instance
    
    # Input the timestamp, return the index of the time
    # The timestamp unit is in seconds
    def index_time(self, start_time, current_time):
        return int((current_time - start_time) / 3600)
    
    # Extract the features from the BGP Update Data
    # TODO: You need to implement a good extractor, including more 
    # prefix-specific features and AS-specific features, instead of this baseline
    def extract_update_features(self, _input_data: pd.DataFrame):
        # Load the BGP Update Data
        df_update_data = _input_data
        # Extract the features from the BGP Update Data
        """Supported Features for each Prefix:
        `num_announce(avg, max, min)`: number of announced times. (Per Hour)
        `num_withdraw(avg, max, min)`: number of withdrawn times. (Per Hour)
        You should implement your own logic here.
        """
        # simple logic we only care about these three fields: "time", "prefix", "as-path"
        dict_prefix_statistics = {}
        # get the start and end time from the dataframe, truncate the data at the hourly time
        start_timestamp = df_update_data['time'].min()
        end_timestamp = df_update_data['time'].max()
        # create bins for the time, using hourly time
        bins = np.arange(start_timestamp, end_timestamp, 3600)
               
        # iterate over the dataframe
        for index, row in df_update_data.iterrows():
            prefix = row['prefix']
            if prefix not in dict_prefix_statistics:
                # setup empty list for the statistics， 0 for announce, 1 for withdraw
                dict_prefix_statistics[prefix] = [[0 for _ in range(len(bins) + 1)], [0 for _ in range(len(bins) + 1)]]
            # get the index of the time
            idx_time = self.index_time(start_timestamp, row['time'])
            if row['type'] == 1:
                dict_prefix_statistics[prefix][0][idx_time] += 1
            elif row['type'] == 2:
                dict_prefix_statistics[prefix][1][idx_time] += 1
        # save the statistics as dataframe, each row contains the start_time, prefix, num_announce, num_withdraw
        list_rows = []
        for prefix, statistics in dict_prefix_statistics.items():
            for i in range(len(bins)):
                list_rows.append([bins[i], prefix, statistics[0][i], statistics[1][i]])
                
        df_features = pd.DataFrame(list_rows, columns=['time', 'prefix', 'num_announce', 'num_withdraw'])
        return df_features
        
feature_extractor = FeatureExtractor()