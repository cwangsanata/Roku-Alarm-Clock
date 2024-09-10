import requests
import time
import schedule
import util as util
import scheduler as scheduler

def main():
    # Load configuration from YAML file
    config = util.load_yaml('config/settings.yaml')
    
    device_ip = config['device']['ip']
    device_port = config['device']['port']
    device_timeout = config['device']['timeout']
    
    video_ids = config['content']['video_ids']
    
    try:
        url = f"http://{device_ip}:{device_port}/launch/837?contentId={video_ids[util.select_random(video_ids)]}"
        response = requests.post(url=url, timeout=device_timeout)
    except ConnectionError as e:
        return response.status_code

if __name__=='__main__':
    scheduler.schedule_tasks(main)
    scheduler.run_schedule()
