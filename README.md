# Pipedrive API v2 Python Client

A Python client library for interacting with the Pipedrive API v2.

This library aims to provide a convenient and Pythonic interface to the Pipedrive API v2, including support for common resources and leveraging Pydantic for data validation and modeling.

## Features

*   Client initialization with API token and company domain.
*   Support for Pipedrive API v2 endpoints.
*   Resource handlers for:
    *   Activities
    *   Deals
    *   Deal Products
    *   Organizations
    *   Persons
    *   Products
    *   Product Variations
    *   Pipelines
    *   Stages
    *   Search (including item search and field search)
*   Pydantic models for request data validation (`CreateModel`, `UpdateModel`).
*   Automatic handling of pagination parameters (`limit`, `cursor`).
*   Custom exception hierarchy for Pipedrive API errors.
*   Handles `None` parameters automatically.
*   Basic request timeout and network error handling.

## Requirements

*   Python 3.7+
*   `requests` library
*   `pydantic` library (v1.x used in current implementation)
*   `python-dotenv` (for loading environment variables in examples)

## Installation

```bash
pip install -r requirements.txt
# Or manually:
# pip install requests pydantic "pydantic<2" python-dotenv
```

*Note: This library currently uses Pydantic v1.x. Ensure compatibility if integrating with projects using Pydantic v2.*

## Usage

### Initialization

First, you need your Pipedrive API token and your company domain (the subdomain part of your Pipedrive URL, e.g., `mycompany` if your URL is `mycompany.pipedrive.com`).

It's recommended to store these securely, for example, using environment variables.

```python
# main.py
import os
from dotenv import load_dotenv
from pipedrive_client import PipedriveV2Client, PipedriveAPIError

# Load environment variables from .env file
load_dotenv()

# Get credentials
api_token = os.getenv('PD_API_TOKEN')
company_domain = os.getenv('PD_COMPANY_DOMAIN') # e.g., 'mycompany'

if not api_token or not company_domain:
    raise ValueError("Please set PD_API_TOKEN and PD_COMPANY_DOMAIN in your .env file")

# Initialize the client
try:
    client = PipedriveV2Client(api_token=api_token, company_domain=company_domain)
    print("Client initialized successfully.")
except ValueError as e:
    print(f"Initialization error: {e}")

```

### Making API Calls

Access different Pipedrive resources through attributes of the client object.

**Example: Listing Deals**

```python
try:
    # List the first 10 open deals
    response = client.deals.list_deals(limit=10, status='open', sort_by='add_time', sort_direction='desc')
    
    if response.get('data'):
        print(f"Found {len(response['data'])} deals:")
        for deal in response['data']:
            print(f"- ID: {deal['id']}, Title: {deal['title']}, Value: {deal.get('value')} {deal.get('currency')}")
            
    # Check for pagination
    if response.get('additional_data', {}).get('pagination', {}).get('next_cursor'):
        next_cursor = response['additional_data']['pagination']['next_cursor']
        print(f"Next cursor for pagination: {next_cursor}")
        # You can use this cursor in the next call: client.deals.list_deals(cursor=next_cursor, ...)
        
except PipedriveAPIError as e:
    print(f"API Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

```

**Example: Creating a Person**

You can pass data as a dictionary or use the provided Pydantic models for validation and type hinting.

```python
# Using a dictionary
person_data_dict = {
    "name": "Jane Doe",
    "owner_id": 1, # Replace with a valid user ID
    "org_id": 12,  # Replace with a valid organization ID
    "email": [{"value": "jane.doe@example.com", "label": "work", "primary": True}],
    "phone": [{"value": "1234567890", "label": "work"}],
    "visible_to": 3 # Owner visibility group
}

# Using Pydantic model
from pipedrive_client.models.persons import PersonCreateModel, PhoneEmailIMValue

person_data_model = PersonCreateModel(
    name="John Smith",
    owner_id=1,
    org_id=15,
    emails=[PhoneEmailIMValue(value="john.smith@example.com", label="work", primary=True)],
    visible_to=1 # Owner & followers
)

try:
    # Using the dictionary
    # created_person = client.persons.create_person(data=person_data_dict)
    # print(f"Created person (dict): ID {created_person['data']['id']}")

    # Using the model
    created_person_model = client.persons.create_person(data=person_data_model)
    print(f"Created person (model): ID {created_person_model['data']['id']}")

except PipedriveAPIError as e:
    print(f"API Error creating person: {e}")
except ValueError as e:
     print(f"Validation Error: {e}") # Catches Pydantic validation errors
except Exception as e:
    print(f"An unexpected error occurred: {e}")

```

**Example: Updating a Deal**

```python
from pipedrive_client.models.deals import DealUpdateModel

deal_id_to_update = 1 # Replace with an actual Deal ID

update_data = DealUpdateModel(
    title="Updated Deal Title",
    status="won",
    value=5000.00,
    currency="USD"
)

try:
    updated_deal = client.deals.update_deal(deal_id=deal_id_to_update, data=update_data)
    print(f"Updated deal: ID {updated_deal['data']['id']}, Status: {updated_deal['data']['status']}")
except PipedriveNotFoundError:
    print(f"Deal with ID {deal_id_to_update} not found.")
except PipedriveAPIError as e:
    print(f"API Error updating deal: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

```

**Example: Searching Items**

```python
try:
    # Search for deals containing "Acme Corp"
    search_results = client.search.search_deals(term="Acme Corp", limit=5)
    
    if search_results.get('data', {}).get('items'):
        print("Deal search results:")
        for item in search_results['data']['items']:
            print(f"- ID: {item['item']['id']}, Title: {item['item']['title']}")
    else:
        print("No deals found matching 'Acme Corp'.")

    # Search across multiple types
    item_search_results = client.search.search_items(term="johndoe@example.com", item_types="person,deal", limit=10)
    if item_search_results.get('data', {}).get('items'):
        print("\nItem search results for 'johndoe@example.com':")
        for item in item_search_results['data']['items']:
            print(f"- Type: {item['item_type']}, ID: {item['item']['id']}, Name/Title: {item['item'].get('name') or item['item'].get('title')}")
    else:
        print("No items found matching 'johndoe@example.com'.")

except PipedriveAPIError as e:
    print(f"API Error during search: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```

## Roadmap

The future development plans, including testing priorities, helper method additions, and potential backward compatibility considerations, are outlined in the [Project Roadmap](ROADMAP.md).

## Error Handling

The client raises specific exceptions based on the HTTP status code returned by the Pipedrive API. All exceptions inherit from `PipedriveAPIError`.

*   `PipedriveAPIError`: Base class for all API errors.
*   `PipedriveAuthError`: For 401/403 errors (authentication/authorization issues).
*   `PipedriveNotFoundError`: For 404 errors (resource not found).
*   `PipedriveValidationError`: For 400/422 errors (invalid input data).
*   `PipedriveRateLimitError`: For 429 errors (rate limit exceeded).
*   `PipedriveServerError`: For 5xx errors (server-side issues).
*   `PipedriveNetworkError`: For network connectivity issues (wraps `requests.exceptions.RequestException`).
*   `PipedriveParseError`: If the API response is not valid JSON.

You can catch specific errors or the base `PipedriveAPIError`.

```python
try:
    # Perform an API call that might fail
    non_existent_deal = client.deals.get_details(deal_id=999999999)
except PipedriveNotFoundError:
    print("Deal not found, as expected.")
except PipedriveAuthError:
    print("Authentication failed. Check your API token.")
except PipedriveRateLimitError:
    print("Rate limit exceeded. Please wait before making more requests.")
except PipedriveAPIError as e:
    print(f"A Pipedrive API error occurred: {e.status_code} - {e.message}")
    # Access raw response data if needed:
    # print(e.response_data)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests. For detailed guidelines on setting up the development environment, running tests, coding style, and submitting changes, please refer to the [Contributing Guide](CONTRIBUTING.md).

## License

This project is licensed under the MIT License - see the LICENSE file for details (if one exists, otherwise specify).