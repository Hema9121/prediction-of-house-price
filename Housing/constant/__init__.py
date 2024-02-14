import os
from datetime import datetime


def get_current_time_stamp():
    return f"{datetime.now().strftime('%d/%m/%Y-%H:%M:%S')}"

#CURRENT_TIME_STAMP = get_current_time_stamp()
#print(CURRENT_TIME_STAMP)