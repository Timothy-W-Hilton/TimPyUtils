"""demo module to check that ffmpeg is available before creating an
animation

"""
import subprocess
import os


def check_for_ffmpeg():
    """Return True if ffmpeg is present on the system.  If ffmpeg is not
    present print a message and return False.

    """

    not_found_msg = """
    The mencoder command was not found;
    mencoder is used by this script to make an mp4 file from a set of
    images. It is typically not installed by default on linux distros
    because of legal restrictions, but it is widely available.  """

    FNULL = open(os.devnull, 'w')
    return_code = None

    try:
        return_code = subprocess.check_call(['ffmpeg', '-h'],
                                            stdout=FNULL,
                                            stderr=subprocess.STDOUT)
    except OSError:
        print not_found_msg

    return return_code is 0
