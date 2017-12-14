"""functions to help separate paths to components

splitall() returns a list of strings, each string containing one
component of the path.

to_ospathjoin() wraps the components into an os.path.join() call

splitpath.splitall() is from `Python Cookbook <https://www.safaribooksonline.com/library/view/python-cookbook/0596001673/ch04s16.html>`_ by David Ascher, Alex Martelli, accessed 31 Mar 2017

"""

import os


def splitall(path):
    """split path into a list of strings, one path component per string

    ARGS:
        path (str): a path

    RETURNS:
        a list of strings, one path component per string

    EXAMPLE:
        >>> splitall('/some/path/to/some/file.txt')
            ['/', 'some', 'path', 'to', 'some', 'file.txt']

    Authors: David Ascher and Alex Martelli, published in `Python
    Cookbook
    <https://www.safaribooksonline.com/library/view/python-cookbook/0596001673/ch04s16.html>`_
    """
    allparts = []
    while 1:
        parts = os.path.split(path)
        if parts[0] == path:  # sentinel for absolute paths
            allparts.insert(0, parts[0])
            break
        elif parts[1] == path:  # sentinel for relative paths
            allparts.insert(0, parts[1])
            break
        else:
            path = parts[0]
            allparts.insert(0, parts[1])
    return(allparts)


def to_ospathjoin(path):
    """reformat a path to a os.path.join call

    ARGS:
        path (str): a path

    RETURNS:
        a string containing the elements of path wrapped in a call to
        os.path.join()

    EXAMPLE:
        >>> to_ospathjoin('/some/path/to/some/file.txt')
            "os.path.join('/', 'some', 'path', 'to', 'some', 'file.txt')"

    Author: Timothy W. Hilton, UC Merced
    """
    components = splitall(path)
    cmd = "os.path.join('{}'".format(components[0])
    for this in components[1:]:
        cmd = cmd + ", '{}'".format(this)
    cmd = cmd + ')'
    return(cmd)
