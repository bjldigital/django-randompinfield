# django-randompinfield

Generates a random pin for your Django model field.

## Installation
Install via pip:

``` bash
pip install django-randompinfield
```

Add to your installed apps:
``` python
INSTALLED_APPS = (
    ...
    'randompinfield',
    ...
)
```


## Usage
Import ```RandomPinField``` into your ```models.py```.

``` python
from django.db import models
from randompinfield import RandomPinField

class MyModel(models.Model):
    slug = RandomPinField(length=3)
```

The ```length``` is an optional argument.
