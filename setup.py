﻿# -*- coding: utf-8 -*-
"""
PyAbsorp setup file
=================
@Author: Michael Markus Ackermann
"""

from setuptools import setup

settings = {
    'name': 'PyAbsorp',
    'version': '0.1.2',
    'description': 'Sound absorption coefficient models implemented in Python.',
    'url': 'https://github.com/Toktom/PyAbsorp',
    'author': 'Michael Markus Ackermann',
    'author_email': 'dev.toktom@outlook.com',
    'license': 'MIT',
    'install_requires': [
        'numpy>=1.18.1', 
        'scipy>=1.4.1'],
    'packages': ['pyabsorp', 'pyabsorp.models']
    }

setup(**settings)
