django-randompinfield
======================

Generates a random pin for your Django model field.

Installation
------------

Install via pip:

.. code:: bash

  $ pip install django-randompinfield


Add to your installed apps:

.. code:: python

  INSTALLED_APPS = (
      ...
      'randompinfield',
      ...
  )


Usage
------

Import ``RandomPinField`` into your ``models.py``.

.. code:: python

  from django.db import models
  from randompinfield import RandomPinField

  class MyModel(models.Model):
      slug = RandomPinField(length=3)

The ``length`` is an optional argument.
