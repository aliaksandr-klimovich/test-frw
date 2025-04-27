import logging

from .const import FixtureScope

log = logging.getLogger(__name__)

class Fixture:
    """Abstract fixture class."""

    # default fixture scope
    scope = FixtureScope.TEST

    def __init__(self):
        raise RuntimeError('Prohibited to init Fixture')

    def setup(self):
        """Fixture setup. Can be overridden by user."""
        pass

    def cleanup(self):
        """Fixture cleanup. Can be overridden by user."""
        pass
