# from case import TestCase
from case import TestCase


class Fixture:
    scope = 'test'

    instance = None

    # prohibit to create instance of the same fixture multiple times when TestCase instance is created
    #
    def __new__(cls):
        if issubclass(cls , TestCase, ) and issubclass(cls, Fixture):
            pass
        elif issubclass(cls , TestCase, ):
            pass
        elif issubclass(cls, Fixture):
            if cls.instance is None:
                cls.instance = super(Fixture, cls).__new__(cls)
            return cls.instance
        instance = super(Fixture, cls).__new__(cls)
        return instance
        # if cls.instance is None:
        #     cls.instance = super(Fixture, cls).__new__(cls)
        # return cls.instance

    def setup(self):
        pass

    def cleanup(self):
        pass
