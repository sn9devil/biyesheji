import time

def now_time():
    localtime = time.localtime(time.time())
    mon = str(localtime.tm_mon)
    day = str(localtime.tm_mday)
    date = mon + '.' + day
    return date


def time_minus_one(s):
    return str(float(s) - 0.01)


def time_set():
    s = now_time()
    lists = []
    lists.append(s)
    for i in range(4):
        s = time_minus_one(s)
        lists.append(s[0:4])
    return lists