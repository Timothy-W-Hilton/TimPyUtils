"""wrapper functions for input/output tasks
"""

import sys
import os
import os.path
import tempfile


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


def get_temp_filename(dir="SCRATCH", prefix='tmpfile', suffix='.png'):
    """return a name for a temporary file

    This is a wrapper for tempfile.NamedTemporaryFile, and provides
    two enhancements: (1) provides a shorthand to place the temporary
    file in the directory pointed to by the operating system
    environment $SCRATCH.  (2) In addition to creating the temporary
    file returns the full path for easy access from a calling routine.

    ARGS:
        dir (string): full path of directory for the temporary
    	    file. Default is $SCRATCH.
        prefix (string): prefix to place before the random string in
            the filename.  Default is "tmpfile"
        suffix (string): suffix to place after the random string in
            the filename.  Default is ".png"

    RETURNS:
        a string containing the full path to a temporary file

    EXAMPLE:
        >>> tmp_name = get_temp_filename(dir='/tmp', suffix='.txt')

    """

    if dir is "SCRATCH":
        dir = os.environ['SCRATCH']

    with tempfile.NamedTemporaryFile(dir=dir,
                                     prefix=prefix, suffix=suffix) as tmpfile:
        temp_file_name = tmpfile.name

    return temp_file_name
