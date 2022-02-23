from datetime import datetime


def logstamp_to_datetime(datestr):
    return datetime.strptime(datestr, '%Y-%m-%dT%H:%M:%S')
