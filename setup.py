import sys

from setuptools import setup

python_ver = sys.version_info

install_requires = []

# Do not use the attribute names as they are not available in Python 2.6.
if python_ver[0] == 2 and python_ver[1] < 7:
    install_requires += ['ordereddict']

setup(name='py-dag',
      version='3.0.1',
      description='Directed acyclic graph implementation',
      url='https://github.com/thieman/py-dag',
      author='Travis Thieman',
      author_email='travis.thieman@gmail.com',
      license='MIT',
      packages=['dag'],
      install_requires=install_requires,
      test_suite='nose.collector',
      tests_require=['nose'] + install_requires,
      zip_safe=False)
