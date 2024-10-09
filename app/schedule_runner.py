import requests
from . import util
from . import scheduler

DEVICE_PORT = 8060

def main():
    # Load configuration from YAML file
    config = util.load_yaml('config/settings.yaml')
    
    device_ip = config['device']['ip']
    device_timeout = config['device']['timeout']
    video_ids = config['content']['video_ids']
    
    try:
        url = f"http://{device_ip}:{DEVICE_PORT}/launch/837?contentId={util.select_random(video_ids)}"
        response = requests.post(url=url, timeout=device_timeout)
    except ConnectionError as e:
        return response.status_code

def run():
    scheduler.schedule_tasks(main)
    scheduler.run_schedule()
