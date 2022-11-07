from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    __long_description__ = f.read()

__name__ = 'feds.py'
__version__ = '1.2'
__author__ = 'addi00000'
__author_email__ = 'addidix@proton.me'
__short_description__ = 'A feds.lol API wrapper for Python.' 
__url__ = 'https://github.com/addi00000/feds.py'
__license__ = 'AGPL-3.0'

setup(
    name=__name__,
    version=__version__,
    author=__author__,
    author_email=__author_email__,
    description=__short_description__,
    long_description=__long_description__,
    long_description_content_type="text/markdown",
    url=__url__,
    license=__license__,
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[
        'requests',
        'bs4'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
    ],
)