import logging
import sys

log = logging.getLogger('testfrw')
log.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter(
    fmt='[{name}][{levelname}] {message}',
    style='{'
)
handler.setFormatter(formatter)
log.addHandler(handler)
