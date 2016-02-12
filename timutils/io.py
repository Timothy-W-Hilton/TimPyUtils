"""wrapper functions for input/output tasks
"""

import sys
import os
import os.path


def delete_if_exists(fname):
    """remove a file if it exists, with a message to stdout

    ARGS:
        fname (string): full path of the file to be removed

    EXAMPLE:
        >>> delete_if_exists('/path/to/file/file_name.txt')
    """
    if os.path.exists(fname):
        sys.stdout.write('removed {}\n'.format(fname))
        sys.stdout.flush()
        os.remove(fname)
        if os.path.exists(fname):
            raise OSError('delete_if_exists failed: file still exists')
