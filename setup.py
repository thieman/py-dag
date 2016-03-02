from setuptools import setup

setup(name='py-dag',
      version='2.5.0',
      description='Directed acyclic graph implementation',
      url='https://github.com/thieman/py-dag',
      author='Travis Thieman',
      author_email='travis.thieman@gmail.com',
      license='MIT',
      packages=['dag'],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)
