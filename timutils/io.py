import sys
import os
import os.path


def delete_if_exists(fname):
    """remove a file if it exists, with a message to stdout

    ARGS:
        fname (string): full path to the file to be removed
    """
    if os.path.exists(fname):
        sys.stdout.write('removed {}\n'.format(fname))
        sys.stdout.flush()
        os.remove(fname)
        if os.path.exists(fname):
            raise OSError('delete_if_exists failed: file still exists')
