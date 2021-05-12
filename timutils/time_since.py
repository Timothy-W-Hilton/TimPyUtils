import time
from datetime import timedelta

def time_since(t0: float):
    """return a string representing time since a reference point

    The string is in the format HH:MM:SS:MS
    """
    return(str(timedelta(seconds=time.time() - t0)))
