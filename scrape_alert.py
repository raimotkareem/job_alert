import time
import os
from send_email import *
from scrape import *
from apscheduler.schedulers.background import BackgroundScheduler

def job():
    print("welcome")


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    # get__job is a function in scrape.py
    scheduler.add_job(get_job, 'interval', seconds=5)
    # send is a function in send_email.py
    scheduler.add_job(send, 'interval', seconds=120)
    scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
    try:
        # This is here to simulate application activity (which keeps  bthe main thread alive).
        while True:
            time.sleep(4)
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()