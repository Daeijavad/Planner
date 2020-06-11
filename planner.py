import os
import time

while True:
    exec(open(os.path.dirname(__file__) + '.\DailyTime.py').read())
    time.sleep(1200)
    print()
