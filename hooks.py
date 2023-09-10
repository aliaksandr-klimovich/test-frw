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
    pass


def on_before_test_run(function):
    hooks_before_test_run.functions.append(function)


class hooks_after_test_run(hooks):
    pass


def on_after_test_run(function):
    hooks_after_test_run.functions.append(function)
