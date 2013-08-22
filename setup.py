# -*- coding: UTF-8 -*-
 
from setuptools import setup, find_packages
import sys, os

version = '0.1'

requires = [
    'pyramid >= 1.4',
    'alembic >= 0.4.1',
    ]

setup(name='pyramid_retort',
      version=version,
      description="Pyramid Alembic project with basic models and views",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Łukasz Bołdys',
      author_email='mail@utek.pl',
      url='',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=requires,
      entry_points="""
      # -*- Entry points: -*-
      [pyramid.scaffold]
      retort=pyramid_retort:AlembicProjectTemplate
      """,
      )