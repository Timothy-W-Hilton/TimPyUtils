try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'A collection of utilities I find useful',
    'author': 'Timothy W. Hilton',
    'url': 'https://timothy-w-hilton.github.io/TimPyUtils/',
    'download_url': 'https://github.com/Timothy-W-Hilton/TimPyUtils',
    'author_email': 'twhilton@ucsc.edu',
    'version': '1.0',
    'install_requires': ['nose', 'numpy', 'matplotlib', 'gitpython'],
    'packages': ['timutils'],
    'scripts': [],
    'name': 'timutils'
}

setup(**config)
