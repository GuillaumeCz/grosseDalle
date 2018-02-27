#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
  name="GrosseDalle",
  version="0.0.1",
  description="Pour ceux qui ont fait et ne peuvent attendre d'etre devant Le Champ de L'étoile pour attiser l'appetit",
  install_requires=[
    'requests',
    'bs4',
    'lxml'
  ],
  packages=find_packages(),
  entry_points={
    'console_scripts': [
      'r2c=r2c.r2c:main'
    ]
  }
)
