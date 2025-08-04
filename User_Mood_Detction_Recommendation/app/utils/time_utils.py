# utils/time_utils.py

from datetime import datetime, timedelta

# Existing functions (keep them)
def get_current_time_str(format="%Y-%m-%d %H:%M:%S"):
    return datetime.now().strftime(format)

def seconds_since(timestamp_str, format="%Y-%m-%d %H:%M:%S"):
    past_time = datetime.strptime(timestamp_str, format)
    delta = datetime.now() - past_time
    return delta.total_seconds()

def human_readable_duration(seconds):
    duration = timedelta(seconds=seconds)
    return str(duration)

# ✅ Add these missing functions:
def get_time_of_day():
    now = datetime.now().hour
    if 5 <= now < 12:
        return "morning"
    elif 12 <= now < 17:
        return "afternoon"
    elif 17 <= now < 21:
        return "evening"
    else:
        return "night"

def is_recent(timestamp, threshold_minutes=30):
    return (datetime.now() - timestamp) < timedelta(minutes=threshold_minutes)
