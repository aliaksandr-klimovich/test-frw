import sys
import traceback

from logger import log


class ExceptionInfo:
    def __init__(self, exc_type=None, exc_value=None, exc_tb=None):
        self.exc_type = exc_type
        self.exc_value = exc_value
        self.exc_tb = exc_tb

    def __repr__(self):
        # todo: provide exc_tb
        return f'exc_type={self.exc_type.__name__}, exc_value="{self.exc_value}", exc_tb="..."'


def get_exc_info() -> ExceptionInfo:
    # get exception info
    exc_type, exc_value, exc_tb = sys.exc_info()
    # skip if no exception was raised
    if exc_tb is None:
        return ExceptionInfo()
    # extract traceback from exception
    tb = traceback.extract_tb(exc_tb)
    f_tb = tb.format()
    rf_tb = reversed(f_tb)
    srf_tb = ''.join(rf_tb)
    # log exception with its traceback info
    log.error(f'{exc_type.__name__}: {exc_value}\n{srf_tb}')
    # store exception info in class
    exc_info = ExceptionInfo(exc_type=exc_type, exc_value=exc_value, exc_tb=srf_tb)
    # remove links
    del exc_type, exc_value, exc_tb
    return exc_info
