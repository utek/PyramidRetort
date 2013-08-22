=================
Retort Scaffold
=================

Retort is a pyramid scaffold. It is based on alchemy scaffold
and includes alembic, basic User model and basic login/logout/register
views.

It also uses mako templating system. And includes jQuery.js, Bootstrap(css only) and Knockout.js


Installation
===============

Clone from github or download package and run::

    python setup.py install

or use pip::

    pip install -e git://github.com/utek/PyramidRetort#egg=PyramidRetort

Check install::

    pcreate -l

Should show something like::

    Available scaffolds:
      alchemy:  Pyramid SQLAlchemy project using url dispatch
      retort:   Pyramid Alembic project with basic models and views
      starter:  Pyramid starter project
      zodb:     Pyramid ZODB project using traversal

Usage
===============

To create new pyramid app using Retort scaffold just run::

    pcreate -s retort <new_project_name>

.. image:: https://d2weczhvl823v0.cloudfront.net/utek/pyramidretort/trend.png
   :alt: Bitdeli badge
   :target: https://bitdeli.com/free

