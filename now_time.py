import time

def now_time():
    localtime = time.localtime(time.time())
    date = str(localtime.tm_mon) + '.' +\
           str(localtime.tm_mday)
    return date