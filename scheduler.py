import schedule
import time
import util as util

def schedule_tasks(func):
    config = util.load_yaml("config/settings.yaml")
    time_zone = config['time']
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
    while True:
        print(schedule.get_jobs())
        schedule.run_pending()
        time.sleep(15)
        