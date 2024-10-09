import schedule
import time
from . import util

def schedule_tasks(func):
    config = util.load_yaml("config/settings.yaml")
    days = config['time']['days']
    
    day_mapping = {
        "monday": schedule.every().monday,
        "tuesday": schedule.every().tuesday,
        "wednesday": schedule.every().wednesday,
        "thursday": schedule.every().thursday,
        "friday": schedule.every().friday,
        "saturday": schedule.every().saturday,
        "sunday": schedule.every().sunday,
    }

    for day_entry in days:
        day, times = list(day_entry.items())[0]  
        if day in day_mapping:
            for time_str in times:
                day_mapping[day].at(time_str).do(func)

def run_schedule():
    last_print_time = time.time()  
    while True:
        schedule.run_pending()
        if time.time() - last_print_time >= 10:
            print(schedule.get_jobs())
            last_print_time = time.time()
        time.sleep(1)
        