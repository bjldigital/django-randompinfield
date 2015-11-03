from distutils.core import setup
setup(
  name = 'django-randompinfield',
  packages = ['randompinfield'], # this must be the same as the name above
  version = '0.1',
  description = 'A django model field that generates a random pin of a desired length',
  author = 'Danny Wilson',
  author_email = 'dannywilson32@gmail.com',
  url = 'https://github.com/bjldigital/', # use the URL to the github repo
  download_url = 'https://github.com/digital', # I'll explain this in a second
  keywords = ['django', 'model', 'field'], # arbitrary keywords
  classifiers = [],
)
