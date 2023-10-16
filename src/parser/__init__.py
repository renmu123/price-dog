from .masadoraSuruga import MasadoraSuruga
from .suruga import Suruga


def parserFactory(name):
    if name == MasadoraSuruga.name:
        return MasadoraSuruga()
    elif name == Suruga.name:
        return Suruga()
    else:
        return None
