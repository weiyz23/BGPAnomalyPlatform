# Flask Backend for BGP Anomaly Detection

## Environment Setup

Install Python 3.8.X for best compatibility with the project.
You can choose other versions of Python 3, but this project is developed using Python 3.8.

The dependencies for the project are listed in the `requirements.txt` file. You can install them using the following command:

```bash
pip install -r requirements.txt
```

## Running the Backend

Run the following command to start the Flask server:

```bash
python -m flask flask run ./app.py --no-reaload --port=<port>
```

Then you can interact with the backend by your frontend application.
The supported requests are listed below.

## The directory structure

The project directory structure is as follows:

```plaintext
.
├── app.py          # The entry point of the Flask application
├── config.py      # The configuration file for the Flask application
├── README.md           # The README file
├── requirements.txt   # The dependencies for the project
├── data                # The directory for storing the BGP data
│   ├── bgp           # The directory for storing the BGP data
│   └── geolocation  # The directory for storing the geolocation data   
└── src
    ├── __init__.py
    ├── utils
    │   ├── __init__.py
    │   ├── bgpstreamer.py  # The util functions for for loading bgp data from BGPstream
    │   ├── geolocator.py  # The util functions for IP geolocation
    |   └── helpers.py  # Helper functions for the project
    ├── outage
    │   ├── __init__.py
    │   ├── detect.py   # The functions for detecting BGP outages
    |   └── extractor.py  # The functions for extracting features from BGP data
    ├── analyze         # Analyse the BGP data, get the AS and prefix information
    │   ├── __init__.py
    │   ├── xxxx.py   # The functions for analysing BGP prefixes
    |   └── yyyy.py   # The functions for analysing BGP ASNs
    ├── models.py   # The models for the project
    └── routes.py   # The routes for the project
```

## Supported Requests

### GET /summary

This endpoint returns a summary of the BGP data, including the number of unique prefixes, the number of unique ASNs, and their latest updates.
Also include the latest BGP outages information.
The frontend can use this information to display the summary of the BGP data (more like a dashboard).

### GET /detail/prefix/

This endpoint returns the detailed information of the given prefix.
The frontend can use this information to display the detailed information of the prefix.


### GET /detail/asn/

This endpoint returns the detailed information of the given ASN.
The frontend can use this information to display the detailed information of the ASN.

<!-- Recommend for Implementation -->

### WS /stream/prefix/

(UNIMPLEMENTED) This endpoint establishes a WebSocket connection to stream the updates of the given prefix.
The frontend can use this information to display the real-time updates of the prefix.

### WS /stream/asn/

(UNIMPLEMENTED) This endpoint establishes a WebSocket connection to stream the updates of the given ASN.
The frontend can use this information to display the real-time updates of the ASN.