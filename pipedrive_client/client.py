import requests
from typing import Optional, Dict, Any, TYPE_CHECKING

from .exceptions import (
    PipedriveAPIError, PipedriveAuthError, PipedriveNotFoundError,
    PipedriveValidationError, PipedriveRateLimitError, PipedriveServerError,
    PipedriveNetworkError, PipedriveParseError
)
from .base import BaseResource
# Import resource classes dynamically if needed, or explicitly
from .areas import (
    Activities, Deals, DealProducts, Organizations, Persons,
    Products, ProductVariations, Pipelines, Stages, Search
)

if TYPE_CHECKING:
    # Avoid circular imports for type hinting
    pass


class PipedriveClient:
    """Generic client for interacting with the Pipedrive API."""

    def __init__(self, api_token: str, company_domain: str, *, api_version: str = "v2"):
        """Create a client for the given API version.

        Args:
            api_token: Pipedrive API token.
            company_domain: Your Pipedrive company domain (e.g. ``"mycompany"`` for ``"mycompany.pipedrive.com"``).
            api_version: ``"v1"`` or ``"v2"``.
        """
        if not api_token:
            raise ValueError("API token cannot be empty.")
        if not company_domain:
            raise ValueError("Company domain cannot be empty.")
        if api_version not in {"v1", "v2"}:
            raise ValueError("api_version must be 'v1' or 'v2'")

        # Remove any protocol or ".pipedrive.com" suffix if provided
        company_domain = (
            company_domain.replace("https://", "").replace("http://", "").replace(".pipedrive.com", "")
        )

        self.api_token = api_token
        self.api_version = api_version
        self.base_url = f"https://{company_domain}.pipedrive.com/api/{api_version}"

        # Use a single session for efficiency
        self.session = requests.Session()
        self.session.headers.update({"x-api-token": self.api_token})

        # Initialize resource handlers
        self.activities = Activities(self)
        self.deals = Deals(self)
        self.deal_products = DealProducts(self)
        self.organizations = Organizations(self)
        self.persons = Persons(self)
        self.products = Products(self)
        self.product_variations = ProductVariations(self)
        self.pipelines = Pipelines(self)
        self.stages = Stages(self)
        self.search = Search(self)

    def _request(
        self,
        method: str,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """
        Makes an HTTP request to the Pipedrive API.

        Args:
            method: HTTP method (GET, POST, PATCH, DELETE).
            path: API endpoint path (e.g., '/deals').
            params: Dictionary of query string parameters.
            data: Dictionary of data for the request body (for POST/PATCH).

        Returns:
            The JSON response from the API as a dictionary.

        Raises:
            PipedriveAPIError: If the API returns an error status code.
            requests.exceptions.RequestException: For network-related errors.
        """
        # Ensure path starts with forward slash
        if not path.startswith('/'):
            path = '/' + path
            
        url = f"{self.base_url}{path}"
        
        try:
            response = self.session.request(
                method,
                url,
                params=self._prepare_params(params) if params else None,
                json=data if data else None,
                timeout=30
            )

            # Check for HTTP errors first
            if not response.ok:
                error_message = ""
                error_data = None
                
                # Try to get detailed error info from response
                try:
                    error_data = response.json()
                    error_message = error_data.get('error', {}).get('message', response.text)
                except requests.exceptions.JSONDecodeError:
                    error_message = response.text or f"HTTP {response.status_code}"
                    error_data = {"raw_response": response.text}
                
                # Map status codes to specific exceptions
                if response.status_code in (401, 403):
                    raise PipedriveAuthError(response.status_code, error_message, error_data)
                elif response.status_code == 404:
                    raise PipedriveNotFoundError(response.status_code, error_message, error_data)
                elif response.status_code in (400, 422):
                    raise PipedriveValidationError(response.status_code, error_message, error_data)
                elif response.status_code == 429:
                    raise PipedriveRateLimitError(response.status_code, error_message, error_data)
                elif response.status_code >= 500:
                    raise PipedriveServerError(response.status_code, error_message, error_data)
                else:
                    raise PipedriveAPIError(response.status_code, error_message, error_data)

            # Handle no content
            if response.status_code == 204 or not response.content:
                return {"success": True, "data": None}

            content_type = response.headers.get("content-type", "")
            if "application/json" in content_type:
                try:
                    return response.json()
                except requests.exceptions.JSONDecodeError as e:
                    raise PipedriveParseError(
                        response.status_code,
                        f"Failed to decode JSON response: {e}",
                        {
                            "raw_response": response.text[:1000],
                            "content_type": content_type,
                            "response_length": len(response.content),
                            "url": url,
                            "method": method,
                        },
                    )

            # Non-JSON response - return raw content
            return {
                "success": True,
                "content": response.content,
                "content_type": content_type,
            }

        except requests.exceptions.RequestException as e:
            # Provide more context for network errors
            raise PipedriveNetworkError(
                0,
                f"Network error occurred: {str(e)}",
                {"url": url, "method": method}
            ) from e

    def _prepare_params(self, params: Optional[Dict[str, Any]]) -> Dict[str, Any]:
        """Removes None values from params dict and converts bools."""
        if params is None:
            return {}
        prepared = {}
        for k, v in params.items():
            if v is not None:
                if isinstance(v, bool):
                    prepared[k] = str(v).lower()  # Convert bool to 'true'/'false'
                elif isinstance(v, list):
                    prepared[k] = ','.join(map(str, v))
                else:
                    prepared[k] = v
        return prepared


class PipedriveV2Client(PipedriveClient):
    """Backward compatible client that defaults to the v2 API."""

    def __init__(self, api_token: str, company_domain: str):
        super().__init__(api_token, company_domain, api_version="v2")

