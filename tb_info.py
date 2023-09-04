import sys
import traceback
from traceback import StackSummary

from logger import log


class TracebackInfo:
    def __init__(self, exc_type=None, exc_value=None, exc_tb=None, stack_info: StackSummary = None):
        self.exc_type = exc_type  # == type(exc_value)
        self.exc_value = exc_value
        self.exc_tb = exc_tb
        if stack_info is not None:
            self.stack_info = ''.join(stack_info.format())
        else:
            self.stack_info = None

    def __repr__(self):
        if self.stack_info is None:
            stack_info = None
        else:
            stack_info = '...'
        return f'exc_type={self.exc_type}, exc_value="{self.exc_value}", exc_tb={self.exc_tb}, stack_info={stack_info}'


def get_tb_info():
    exc_type, exc_value, exc_tb = sys.exc_info()
    stack_info = traceback.extract_stack()
    tb_info = TracebackInfo(exc_type=None, exc_value=exc_value, exc_tb=None, stack_info=stack_info)
    log.error(f'{exc_type.__name__}: {exc_value}', stack_info=True)
    del stack_info, exc_type, exc_value, exc_tb
    return tb_info
