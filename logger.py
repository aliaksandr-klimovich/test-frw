import logging
import sys

logging.basicConfig(
    level=logging.DEBUG,
    stream=sys.stdout,
    format='%(asctime)s %(name)s %(levelname)s -- %(message)s -- File "%(pathname)s", line %(lineno)d, in %(funcName)s',
    datefmt='%Y-%m-%dT%H:%M:%S%z',
)
breakpoint()