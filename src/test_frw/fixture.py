import logging

from .case import TestCase

log = logging.getLogger(__name__)

class Fixture:
    scope = 'test'
    _instance = None

    # prohibit to create instance of the same fixture multiple times
    def __new__(cls):
        if issubclass(cls, TestCase) and issubclass(cls, Fixture):
            pass
        elif issubclass(cls, TestCase):
            pass
        elif cls is Fixture:
            pass
        elif issubclass(cls, Fixture):
            if cls._instance is None:
                cls.instance = super(Fixture, cls).__new__(cls)
            return cls._instance
        instance = super(Fixture, cls).__new__(cls)
        return instance

    def setup(self):
        pass

    def cleanup(self):
        pass
