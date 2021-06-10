

from apscheduler.schedulers.background import BackgroundScheduler
# from .views import index


# sched = BlockingScheduler()
sched = BackgroundScheduler()

def my_job(text):
    print(text)


def job_function():
    print('Running Task')

# The job will be executed on June 10th, 2021 at 08:20:30
sched.add_job(my_job, 'date', run_date='2021-06-10 20:20:30', args=['This task will run at the exact time'])


# Runs from Monday to Friday at 8:32 (pm) until 2021-06-30 00:00:00
sched.add_job(job_function, 'cron', day_of_week='mon-fri', hour=20, minute=32, end_date='2021-06-30')


sched.start()
