try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'A collection of utilities I find useful',
    'author': 'Timothy W. Hilton',
    'url': 'thilton@ucmerced.edu',
    'download_url': 'thilton@ucmerced.edu',
    'author_email': 'thilton@ucmerced.edu',
    'version': '1.0',
    'install_requires': ['nose', 'numpy', 'matplotlib'],
    'packages': ['timutils'],
    'scripts': [],
    'name': 'timutils'
}

setup(**config)
