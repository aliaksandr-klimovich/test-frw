import logging
import sys


log = logging.getLogger('testfrw')

# temporary solution
log.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter(
    fmt='%(asctime)s %(levelname)s %(name)s -- %(message)s -- File "%(pathname)s", line %(lineno)d, in %(funcName)s',
    datefmt='%Y-%m-%dT%H:%M:%S%z'
)
handler.setFormatter(formatter)
log.addHandler(handler)
