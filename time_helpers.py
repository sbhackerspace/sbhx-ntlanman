import datetime
import pytz
import pyrfc3339

def now():
    now_utc = datetime.datetime.utcnow()
    return pyrfc3339.generate(now_utc.replace(tzinfo=pytz.utc))

def parse(now_str):
    return pyrfc3339.parse(now_str)
