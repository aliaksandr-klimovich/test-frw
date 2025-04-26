import logging
import sys

# it's up to user to configure the logger
# this is a solution for debug purposes
logging.basicConfig(
    level=logging.DEBUG,
    stream=sys.stdout,
    # todo log thread name
    format='%(asctime)s %(name)s %(levelname)s -- %(message)s -- File "%(pathname)s", line %(lineno)d, in %(funcName)s',
    datefmt='%Y-%m-%dT%H:%M:%S%z',
)

# test logger
log = logging.getLogger('test')
