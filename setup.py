import sys
from setuptools import setup
from setuptools import find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pyController",
    version="1.0",
    author="Brandon Iams",
    author_email = "jbiams77@uw.edu",
    description="Event Callback system for Bluetooth Controller",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jbiams77/pyController",
    packages=find_packages(),
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities"
    ],
    keywords=["playstation", "ps4", "controller", "robot controls"],
    entry_points={
          'console_scripts': [
              'python2version = pyController.__main__:main'
              if sys.version_info[0] < 3 else
              'python3version = pyController.__main__:main',
          ]
    },
)