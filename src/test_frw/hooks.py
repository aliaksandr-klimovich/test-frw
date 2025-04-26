"""Hooks."""

import logging

log = logging.getLogger(__name__)

class metahooks(type):
    def __init__(cls, name, bases=None, namespace=None):
        super(metahooks, cls).__init__(name, bases, namespace)
        cls.functions = []

class hooks(metaclass=metahooks):
    functions: list

    @classmethod
    def run(cls, *args, **kwargs):
        for function in cls.functions:
            function(*args, **kwargs)

class hooks_before_test_run(hooks):
    """Executes hooks exactly before `run` method of a test case is called."""

def on_before_test_run(function):
    """Decorator for hooks_before_test_run."""
    hooks_before_test_run.functions.append(function)
    # todo: add possibility to insert to the start of the list,
    #  i.e. hooks_before_test_run.functions.insert(0, function),
    #  same for other decorators

class hooks_after_test_run(hooks):
    """Executes hooks exactly after `run` method of a test case is called."""

def on_after_test_run(function):
    """Decorator for hooks_after_test_run."""
    hooks_after_test_run.functions.append(function)
