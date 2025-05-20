from typing import Optional, Dict, Any, Union, List

from ..client import BaseResource
from ..models.persons import PersonCreateModel, PersonUpdateModel

class Persons(BaseResource):
    """
    Encapsulates methods for interacting with the Pipedrive Persons V2 API.
    Ref: https://pipedrive.readme.io/docs/pipedrive-api-v2-migration-guide#persons-api
    """

    def get_details(
        self, person_id: int, *, include_fields: Optional[str] = None, custom_fields: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Returns details of a specific person. (GET /persons/{id})

        Args:
            person_id: The ID of the person.
            include_fields: Comma-separated string of optional fields to include (e.g., 'next_activity_id,files_count').
            custom_fields: Comma-separated string of custom field API keys to include.

        Returns:
            Dictionary representing the person details.
        """
        params = {
            "include_fields": include_fields,
            "custom_fields": custom_fields,
        }
        return self._client._request("GET", f"/persons/{person_id}", params=self._prepare_params(params))

    def list_persons(
        self,
        *,
        owner_id: Optional[int] = None, # Renamed from user_id
        filter_id: Optional[int] = None,
        org_id: Optional[int] = None, # V2 quick filter
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        sort_by: Optional[str] = None, # e.g., 'id', 'name', 'add_time', 'update_time', 'org_id'
        sort_direction: Optional[str] = None, # 'asc', 'desc'
        include_fields: Optional[str] = None,
        custom_fields: Optional[str] = None,
        first_char: Optional[str] = None, # Seems still supported based on some API explorers, though removed from object itself
    ) -> Dict[str, Any]:
        """
        Returns all persons. (GET /persons) Also replaces v1 GET /organizations/:id/persons.

        Args:
            owner_id: If supplied, only persons owned by the given user will be returned.
            filter_id: ID of the filter to use.
            org_id: If supplied, only persons related to the given organization will be returned.
            limit: For pagination, the limit of entries to return.
            cursor: For pagination, the cursor marker from the previous response.
            sort_by: Field to sort by.
            sort_direction: Direction of sorting ('asc', 'desc').
            include_fields: Comma-separated string of optional fields to include.
            custom_fields: Comma-separated string of custom field API keys to include.
            first_char: Optional first character to filter by name (legacy?).

        Returns:
            Dictionary containing list of persons and pagination info.
        """
        params = {
            "user_id": owner_id, # Map owner_id kwarg to user_id param
            "filter_id": filter_id,
            "org_id": org_id,
            "limit": limit,
            "cursor": cursor,
            "sort_by": sort_by,
            "sort_direction": sort_direction,
            "include_fields": include_fields,
            "custom_fields": custom_fields,
            "first_char": first_char,
        }
        return self._client._request("GET", "/persons", params=self._prepare_params(params))

    def create_person(self, data: Union[Dict[str, Any], PersonCreateModel]) -> Dict[str, Any]:
        """
        Creates a new person. (POST /persons)

        Args:
            data: Dictionary or PersonCreateModel object containing person details.
                  Requires 'name' or both 'first_name' and 'last_name'.
                  'emails', 'phones', 'ims' should be lists of objects like [{"value": "...", "label": "...", "primary": True}].

        Returns:
            Dictionary representing the newly created person.
        """
        if isinstance(data, PersonCreateModel):
            # Validate before sending
            data.dict() # This will trigger validation
            payload = data.dict(exclude_unset=True, by_alias=True)
        else:
             # Basic check if dict is passed
             if not data.get('name') and not (data.get('first_name') is not None and data.get('last_name') is not None):
                  raise ValueError('Either "name" or both "first_name" and "last_name" must be provided')
             if not data.get('name') and data.get('first_name') == "" and data.get('last_name') == "":
                 raise ValueError('Both "first_name" and "last_name" cannot be empty if "name" is not provided')
             payload = data

        return self._client._request("POST", "/persons", data=payload)

    def update_person(self, person_id: int, data: Union[Dict[str, Any], PersonUpdateModel]) -> Dict[str, Any]:
        """
        Updates an existing person. (PATCH /persons/{id})

        Args:
            person_id: The ID of the person to update.
            data: Dictionary or PersonUpdateModel object containing fields to update.

        Returns:
            Dictionary representing the updated person.
        """
        if isinstance(data, PersonUpdateModel):
             # Validate before sending if needed, though PATCH allows partial updates
             data.dict(exclude_unset=True) # Trigger validation if needed
             payload = data.dict(exclude_unset=True, by_alias=True)
        else:
             # Basic check if dict is passed
             if data.get('name') is None and (data.get('first_name') == "" and data.get('last_name') == ""):
                 raise ValueError('Both "first_name" and "last_name" cannot be empty if "name" is not provided during update')
             payload = data

        return self._client._request("PATCH", f"/persons/{person_id}", data=payload)

    def delete_person(self, person_id: int) -> Dict[str, Any]:
        """
        Deletes a specific person. (DELETE /persons/{id})
        Note: Migration guide mentions DELETE /api/v{1,2}/persons (plural), assuming deletion by ID.

        Args:
            person_id: The ID of the person to delete.

        Returns:
            Dictionary indicating success or failure.
        """
        return self._client._request("DELETE", f"/persons/{person_id}")