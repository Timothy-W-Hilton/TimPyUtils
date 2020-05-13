"""print the git revision and the python prefix
"""

import sys
from timutils.git_tools import print_cwd_git_version

def print_env():
    """write current directory git revision and python prefix to stdout
    """
    print_cwd_git_version()
    print('python environment: {}'.format(sys.prefix))
