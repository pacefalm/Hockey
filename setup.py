#! /usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="Hockey",
    description="Scraping and analysis of data from NHL and other leagues",
    author="muneebalam",
    author_email="",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "matplotlib",
        "numpy",
    ],
    classifiers=(
        "Development Status :: 5",
        "Fraomework :: Praw",
        "Programming Language :: Python :: 3"
    ),
    platforms="Python 3.4.3 and later."
)

