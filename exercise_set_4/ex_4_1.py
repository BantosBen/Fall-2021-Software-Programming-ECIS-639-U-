from ex_4_0 import get_shutdown_events


def num_shutdowns(logfile):
    shutdowns = get_shutdown_events(logfile)
    shutdown_counts = len(shutdowns) * 2
    return shutdown_counts
