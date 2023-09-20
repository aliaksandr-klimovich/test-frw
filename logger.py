"""Logger."""

import logging
import sys


log = logging.getLogger('test_frw')

# temporary solution
log.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    fmt='%(asctime)s %(levelname)s %(name)s -- %(message)s -- File "%(pathname)s", line %(lineno)d, in %(funcName)s',
    datefmt='%Y-%m-%dT%H:%M:%S%z'
)
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(formatter)
log.addHandler(handler)
