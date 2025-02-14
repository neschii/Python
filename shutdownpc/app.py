
import schedule
import time
import os


def shutdownpc():
    os.system("shutdown /r /t 0")
    
schedule.every().hour.at(":53").do(shutdownpc)

while True:
    schedule.run_pending()
    time.sleep(1)


