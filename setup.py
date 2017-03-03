try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
  name='log_parser',
  packages=[
        'log_parser',
  ],
  version='0.1',
  scripts=['log_parser/log_parser'],
  description='Tool to parse access log by IP/CIDR address',
  author='Binh Nguyen',
  author_email='',
  license='apache 2.0',
  keywords=['log', 'parser'],
  url='',
  classifiers=[
        "Development Status :: Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Topic :: System :: Systems Administration",
        "Topic :: Utilities"
  ],
  install_requires=[
  'netaddr',
  'argparse',
  'pytest'
  ],
)
