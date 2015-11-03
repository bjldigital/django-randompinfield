from django.core.exceptions import FieldError
from django.db.models import IntegerField

from random import randint

class RandomPinField(IntegerField):
    """
    Generates a random digit pin

    By default sets length=4

    Optional arguments:
        length
            Integer for how long the pin will be. (default=4)
    """

    def __init__(self, length=4, *args, **kwargs):

        self.length = length

        kwargs.setdefault('max_length', self.length)
        if kwargs['max_length'] < self.length:
            raise ValueError("'max_length' must be equal to or greater than "
                             "'length'.")

        super(RandomPinField, self).__init__(*args, **kwargs)


    def generate_pin(self, model_instance):
        """
        Returns a random pin.
        """

        range_start = 10**(self.length - 1)
        range_end = (10**self.length) - 1

        return randint(range_start, range_end)

    def pre_save(self, model_instance, add):
        value = getattr(model_instance, self.attname)
        if not value:
            value = self.generate_pin(model_instance)
            setattr(model_instance, self.attname, value)
        return value

    def deconstruct(self):
        name, path, args, kwargs = super(RandomPinField, self).deconstruct()
        if self.length != 4:
            kwargs['length'] = self.length
        return name, path, args, kwargs
