"""
Pipedrive API v2 Python Client
"""
from .client import PipedriveV2Client
from .exceptions import PipedriveAPIError

__all__ = ["PipedriveV2Client", "PipedriveAPIError"]
__version__ = "0.1.0"