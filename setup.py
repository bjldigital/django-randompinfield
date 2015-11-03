from distutils.core import setup

f = open('README.rst', 'r')

setup(
  name = 'django-randompinfield',
  packages = ['randompinfield'],
  version = '0.4.4',
  license="MIT",
  description = 'A django model field that generates a random pin of a desired length',
  long_description=f.read(),
  author = 'Danny Wilson',
  author_email = 'dannywilson32@gmail.com',
  url = 'https://github.com/bjldigital/django-randompinfield/',
  download_url = 'https://github.com/bjldigital/django-randompinfield/archive/v0.4.4.tar.gz',
  keywords = ['django', 'model', 'field'],
  classifiers = [
    "Framework :: Django",
    "Environment :: Web Environment",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2.7"
  ],
)
