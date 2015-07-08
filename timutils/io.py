import sys
import os
import os.path


def delete_if_exists(fname):
    """remove a file if it exists, with a message to stdout
    """
    if os.path.exists(fname):
        sys.stdout.write('removed {}\n'.format(fname))
        sys.stdout.flush()
        os.remove(fname)
        if os.path.exists(fname):
            raise OSError('file still exists')
