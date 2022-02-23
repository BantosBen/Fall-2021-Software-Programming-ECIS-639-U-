def get_shutdown_events(logfile):
    shutdowns = list()
    file_handler = open(logfile, 'r')
    for log in file_handler:
        if 'Shutdown initiated' in log:
            shutdowns.append(log)
    file_handler.close()
    return shutdowns
