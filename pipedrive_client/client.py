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


class PipedriveV2Client:
    """
    A client for interacting with the Pipedrive API v2.
    """
    def __init__(self, api_token: str, company_domain: str):
        """
        Initializes the Pipedrive API v2 client.

        Args:
            api_token: Your Pipedrive API token.
            company_domain: Your Pipedrive company domain (e.g., 'mycompany' for 'mycompany.pipedrive.com').
        """
        if not api_token:
            raise ValueError("API token cannot be empty.")
        if not company_domain:
            raise ValueError("Company domain cannot be empty.")
            
        # Remove any protocol or .pipedrive.com suffix if provided
        company_domain = company_domain.replace('https://', '').replace('http://', '').replace('.pipedrive.com', '')
        
        self.api_token = api_token
        # Update base_url to include /api/v2
        self.base_url = f"https://{company_domain}.pipedrive.com/api/v2"
        # Simplify headers setup
        self.headers = {"x-api-token": self.api_token}

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
            response = requests.request(
                method,
                url,
                headers=self.headers,
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

            # Handle successful responses that might have no content
            if response.status_code == 204:
                return {"success": True}

            # For successful responses, ensure we have content
            if not response.content:
                return {"success": True, "data": None}

            # Try to parse JSON response
            try:
                return response.json()
            except requests.exceptions.JSONDecodeError as e:
                # Include response details in error for debugging
                raise PipedriveParseError(
                    response.status_code,
                    f"Failed to decode JSON response: {e}",
                    {
                        "raw_response": response.text[:1000],  # Limit raw response length
                        "content_type": response.headers.get('content-type'),
                        "response_length": len(response.content),
                        "url": url,
                        "method": method
                    }
                )

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
                    prepared[k] = str(v).lower() # Convert bool to 'true'/'false' strings for params
                elif isinstance(v, list):
                     prepared[k] = ','.join(map(str, v))
                else:
                    prepared[k] = v
        return prepared