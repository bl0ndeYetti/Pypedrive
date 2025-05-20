from typing import Optional, Dict, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .client import PipedriveClient

class BaseResource:
    """Base class for API resource endpoints."""
    def __init__(self, client: 'PipedriveClient'):
        self._client = client

    def _prepare_params(self, params: Optional[Dict[str, Any]]) -> Dict[str, Any]:
        """Removes None values from params dict."""
        if params is None:
            return {}
        return {k: v for k, v in params.items() if v is not None} 
