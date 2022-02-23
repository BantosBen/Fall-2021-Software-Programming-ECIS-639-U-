from ex_4_1 import get_shutdown_events
from ex_4_2 import logstamp_to_datetime


def time_between_shutdowns(logfile):
    shutdowns = get_shutdown_events(logfile)
    initial = shutdowns[0]
    final = shutdowns[-1]

    initial_datestr = initial.split(' ')[1]
    final_datestr = final.split(' ')[1]

    initial_date = logstamp_to_datetime(initial_datestr)
    final_date = logstamp_to_datetime(final_datestr)

    time_difference = final_date - initial_date
    return time_difference
