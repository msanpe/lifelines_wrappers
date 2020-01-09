#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

exec(compile(open('lifelines_wrappers/__init__.py').read(),
             'lifelines_wrappers/__init__.py', 'exec'))

setup(name='lifelines_wrappers',
      version=__version__,
      description='sklearn estimator wrappers for lifelines survival analysis from CamDavidsonPilon/lifelines',
      maintainer='Miguel Sancho Peña',
      maintainer_email='msancho@ibm.com',
      packages=['lifelines_wrappers'],
      keywords=['sklearn', 'lifelines'],
      install_requires=[
          'lifelines >= 0.8.0.2',
          'scikit-learn>=0.13',
          'pandas>=0.11.0'],
      )
