from typing import Optional, Dict, Any

class PipedriveAPIError(Exception):
    """Base exception for Pipedrive API errors."""

    def __init__(self, status_code: int, message: str, response_data: Optional[Dict[str, Any]] = None):
        self.status_code = status_code
        self.message = message
        self.response_data = response_data or {}
        super().__init__(self.__str__())

    def __str__(self) -> str:
        error_msg = f"Pipedrive API Error {self.status_code}: {self.message}"
        if self.response_data:
            # Format error details more cleanly
            details = []
            for key, value in self.response_data.items():
                if key != "raw_response" or len(str(value)) < 100:  # Don't include long raw responses
                    details.append(f"{key}: {value}")
            if details:
                error_msg += f"\nDetails: {', '.join(details)}"
        return error_msg

class PipedriveAuthError(PipedriveAPIError):
    """Raised for authentication and authorization errors (401, 403)."""
    pass

class PipedriveNotFoundError(PipedriveAPIError):
    """Raised when a resource is not found (404)."""
    pass

class PipedriveValidationError(PipedriveAPIError):
    """Raised for validation errors (400, 422)."""
    pass

class PipedriveRateLimitError(PipedriveAPIError):
    """Raised when API rate limit is exceeded (429)."""
    pass

class PipedriveServerError(PipedriveAPIError):
    """Raised for server-side errors (500, 502, 503, 504)."""
    pass

class PipedriveNetworkError(PipedriveAPIError):
    """Raised for network-related errors."""
    pass

class PipedriveParseError(PipedriveAPIError):
    """Raised when response parsing fails."""
    pass