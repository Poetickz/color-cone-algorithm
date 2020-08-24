#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

requirements = [
    # TODO: put package requirements here
    "colormath==3.0.0"
    "numpy==1.19.1"
    "scikit-learn==0.23.2"
    "opencv-python==4.4.0"
    "joblib==0.16.0"
]

setup_requirements = [
    # TODO put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    # TODO: put package test requirements here
]

desc = "Color Cone Algorithm with python & opencv"
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='color-cone-algorithm',
    version=__version__,
    description=desc,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Alan Rocha, Diego Aragón and Steve Albo",
    author_email='alan.rocha@udem.edu, diego.aragon@udem.edu and guillermo.albo@udem.edu ',
    url='https://github.com/Poetickz/color-cone-algorithm',
    packages=find_packages(include=['color-cone-algorithm']),
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='color blind',
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements
)
