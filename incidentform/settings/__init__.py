from .common import *
from .auth import *
from .logging import *

try:
    from .dev import *
    _DEVELOPMENT = True
except ImportError:
    _DEVELOPMENT = False


assert _DEVELOPMENT, "Bad settings: development {0}".format(_DEVELOPMENT)
