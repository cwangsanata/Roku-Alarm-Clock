import requests
import os
import yaml
import logging
from util.connector import Connector

CLIENT_NAME="roku_tv_main_bedroom"
IP="192.168.0.14"
PORT=8060

def main():
    # Load configuration from YAML file
    with open('/config/settings.yaml', 'r') as file:
        config = yaml.safe_load(file)

    # Use environment variables if available, otherwise use config file
    device_ip = os.getenv('DEVICE_IP', config['device']['ip'])
    device_port = os.getenv('DEVICE_PORT', config['device']['port'])
    device_timeout = config['device']['timeout']

    # TODO: Change to logging
    print(f"Connecting to device at {device_ip}:{device_port} with a timeout of {device_timeout} seconds.")

    # Send the request
    r = requests()


    