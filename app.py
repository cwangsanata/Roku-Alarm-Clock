import requests
import os
import yaml
from util import select_random
# import logging

def main():
    # Load configuration from YAML file
    with open('config/settings.yaml', 'r') as file:
        config = yaml.safe_load(file)

    device_ip = os.getenv('DEVICE_IP', config['device']['ip'])
    device_port = os.getenv('DEVICE_PORT', config['device']['port'])
    device_timeout = config['device']['timeout']
    
    video_ids = config['content']['video_ids']

    # TODO: Change all prints to logging and print too
    print(f"Attempting to connect to device at {device_ip}:{device_port} with a timeout of {device_timeout} seconds.")
    
    # TODO: Add logging here for connection
    try:
        url = f"http://{device_ip}:{device_port}/launch/837?contentId={video_ids[select_random(video_ids)]}"
        response = requests.post(url=url, timeout=device_timeout)
    except ConnectionError as e:
        print(e)

    print(response)

if __name__=='__main__':
    main()


    