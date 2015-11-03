from distutils.core import setup

with open('README.md') as f:
    readme = f.read()

setup(
  name = 'django-randompinfield',
  packages = ['randompinfield'],
  version = '0.2',
  license="MIT",
  description = 'A django model field that generates a random pin of a desired length',
  long_description=readme,
  author = 'Danny Wilson',
  author_email = 'dannywilson32@gmail.com',
  url = 'https://github.com/bjldigital/django-randompinfield/',
  download_url = 'https://github.com/bjldigital/django-randompinfield/archive/v0.1.tar.gz',
  keywords = ['django', 'model', 'field'],
  classifiers = [
    "Framework :: Django",
    "Environment :: Web Environment",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2.7"
  ],
)
