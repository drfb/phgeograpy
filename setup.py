# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from phgeograpy.__version__ import VERSION

with open('README.md') as f:
    readme = f.read()

setup(
    name='phgeograpy',
    version=VERSION,
    description='A python package that lists regions, provinces, and cities/municipalities in the Philippines',
    long_description=readme,
    author='Dhan-Rheb Belza',
    author_email='dhanrheb@gmail.com',
    url='https://github.com/drfb/phgeograpy',
    license='MIT',
    packages=find_packages(),
    keywords='philippine geography regions provinces cities municipalities',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
