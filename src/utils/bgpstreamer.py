# ==============================================
# Utils functions for BGP Stream
# You can implement your own logic here
# ==============================================

# Import the built-in libraries
import re
import subprocess
import time
import asyncio
from concurrent import futures
from datetime import datetime, timedelta

# Import the third-party libraries
import pybgpstream

# Import the customized libraries
from src.utils.helpers import *

MESSGATE_TYPE_MAPPER = {
    "A": 1,     # Announce
    "W": 2,     # Withdraw
    "R": 3,     # RIB Info
    "S": 4,     # Peer State Change
    "B": 5,     # BGP State Change (?)
    "D": 6,     # Data Plane Change (?)
    "N": 7      # Unknown (?)
}

PROJECT_MAPPER = {
    "routeviews": 1,
    "ris": 2,
    "routeviews-stream": 3,
    "ris-live": 4,
}


"""RouteViews data update frequency:

The FRR files (RIBS and UPDATES) have different intervals. 
RIBS are snapshots and are collected **every 2 hours** 
UPDATES are ongoing files that are rotated **every 15 minutes** 
These intervals begin when the daemon is started, not from some specific time.

The filter pattern is detailed in the BGPStream documentation, see https://github.com/CAIDA/libbgpstream/blob/master/FILTERING.
More BGP data tools can be found in https://ris.ripe.net/docs/mrt/#name-and-location.
"""


def get_bgp_historical_update_data(
    _from: datetime,
    _until: datetime,
    _collector: list = ["rrc06"],
    _filter: str = "ipv 4"
    ):
    """Collected BGP Update Messages.
    BGP Update Messages are the messages exchanged between BGP routers to convey reachability information
    You can use them to analyze the evolution of the global routing.
    """
    # If _from is None, return the last 15 mins data
    assert _until is not None, "Please specify the end time."
    if _from is None:
        _from = datetime.now() - timedelta(seconds=900)
    _from_str = _from.strftime("%Y-%m-%d %H:%M:%S")
    _until_str = _until.strftime("%Y-%m-%d %H:%M:%S")
    return bgp_stream_historic_basic(
        _from_str=_from_str, 
        _until_str=_until_str, 
        _type="updates",
        _collector=_collector, 
        _filter=_filter
        )


def get_bgp_historical_rib_data(
    _from: datetime,
    _until: datetime,
    _collector: list = ["rrc06"],
    _filter: str = "ipv 4"
    ):
    """BGP Data in the RIBs, not the updates.
    BGP RIBs (Routing Information Bases) are the tables used by BGP routers to make routing decisions.
    You can use them to analyze the current global routing table.
    """
    # If _from is None, return the last 2 hours data
    assert _until is not None, "Please specify the end time."
    if _from is None:
        _from = datetime.now() - timedelta(seconds=7200)
    _from_str = _from.strftime("%Y-%m-%d %H:%M:%S")
    _until_str = _until.strftime("%Y-%m-%d %H:%M:%S")
    return bgp_stream_historic_basic(
        _from_str=_from_str, 
        _until_str=_until_str, 
        _type="ribs",
        _collector=_collector, 
        _filter=_filter
        )


def get_bgp_live_update_data(
    _project: str = "routeviews-stream", 
    _filter: str = "ipv 4 and router amsix"):
    """ Basic Function for fetching live BGP Update Data
    You can use the returned object to fetch the data
    ** Note: Need some time to fetch the data... **
    """
    if _filter is None:
        return pybgpstream.BGPStream(
            project=_project
        )
    
    return pybgpstream.BGPStream(
        project=_project,
        filter=_filter
    )


def bgp_stream_historic_basic(
    _from_str: str = "2021-09-01 00:00:00", 
    _until_str: str = "2021-09-01 00:00:30",
    _collector: list = ["rrc06"], 
    _type: str = "updates", 
    _filter: str = "ipv 4"):
    """ Basic Function for fetching BGP Data (RIB or Update) in a specific time interval
    You can use the returned object to fetch the data
    ** Note: Need some time to fetch the data... **
    """
    return pybgpstream.BGPStream(
    from_time=_from_str,
    until_time=_until_str,
    collectors=_collector,
    record_type=_type,
    filter=_filter
    )


NUM_PATTERN = re.compile(r"(\d+)")
def parse_as_path_string(as_path: str) -> list:
    """Parse the AS Path String to a list of ASNs
    Sometimes their are parens in the AS Path such as "{123 456 789}"
    (): AS_CONFED_SEQUENCE, ordered set of ASes
    []: AS_CONFED_SET, unordered set of ASes
    {}: AS_SET, unordered set of ASes
    None: AS_SEQUENCE, ordered set of ASes
    CHALLENGE: We just treat all of them as AS_SEQUENCE, you can implement your own logic here
    """
    as_path_list = []
    if as_path is not None:
        as_path_list = [int(asn) for asn in NUM_PATTERN.findall(as_path)]
    return as_path_list

# Parse the bgp data in the elem, return the parsed data
# You can implement your own logic here
def parse_the_bgp_data(elem: pybgpstream.BGPElem) -> dict:
    """Possible Fileds:
    Required: record_type, type, time, project, collector, router, router_ip, peer_asn, peer_address,
    Optional: prefix, next-hop, as-path, communities , old-state, new-state
    """
    elem_item = {}
    # the original fields are modified for better memory performance.
    if elem.record_type == "update":
        elem_item = {
            "update": True,
            "type": MESSGATE_TYPE_MAPPER[elem.type],
            "time": elem.time,
            "project": PROJECT_MAPPER[elem.project],
            "collector": elem.collector,
            "router": elem.router,
            "router_ip": elem.router_ip if elem.router_ip is None else ip_to_int(elem.router_ip),
            "peer_asn": elem.peer_asn,
            "peer_address": elem.peer_address if elem.peer_address is None else ip_to_int(elem.peer_address),
            "prefix": elem._maybe_field("prefix"),
            "next-hop": elem._maybe_field("next-hop") if elem._maybe_field("next-hop") is None else ip_to_int(elem._maybe_field("next-hop")),
            "as-path": parse_as_path_string(elem._maybe_field("as-path")),
            # We ignore some fields
        }
    elif elem.record_type == "rib":
        # TODO: You can implement your own logic here
        pass
    return elem_item

# TODO: Although there are many helpful functions, maybe you need your own implementation here.