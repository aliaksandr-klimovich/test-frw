import logging
import sys

log = logging.getLogger('testfrw')
log.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    fmt='[%(levelname)s] %(message)s',
    # fmt='[%(asctime)s][%(levelname)s] %(message)s',
    # datefmt='%Y-%m-%dT%H:%M:%S'
)  # todo: revert is needed
handler.setFormatter(formatter)
log.addHandler(handler)
