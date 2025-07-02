from datetime import datetime

def generate_time():
    return datetime.now()

def duration(start_time):
    return print('Duration: {}'.format( datetime.now() - start_time))