from typing import Optional, Dict, Any, Union, List

from ..client import BaseResource
from ..models.organizations import OrganizationCreateModel, OrganizationUpdateModel

class Organizations(BaseResource):
    """
    Encapsulates methods for interacting with the Pipedrive Organizations V2 API.
    Ref: https://pipedrive.readme.io/docs/pipedrive-api-v2-migration-guide#organizations-api
    """

    def get_details(
        self, org_id: int, *, include_fields: Optional[str] = None, custom_fields: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Returns details of a specific organization. (GET /organizations/{id})

        Args:
            org_id: The ID of the organization.
            include_fields: Comma-separated string of optional fields to include (e.g., 'next_activity_id,files_count').
            custom_fields: Comma-separated string of custom field API keys to include.

        Returns:
            Dictionary representing the organization details.
        """
        params = {
            "include_fields": include_fields,
            "custom_fields": custom_fields,
        }
        return self._client._request("GET", f"/organizations/{org_id}", params=self._prepare_params(params))

    def list_organizations(
        self,
        *,
        owner_id: Optional[int] = None, # Renamed from user_id
        filter_id: Optional[int] = None,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        sort_by: Optional[str] = None, # e.g., 'id', 'name', 'add_time', 'update_time'
        sort_direction: Optional[str] = None, # 'asc', 'desc'
        include_fields: Optional[str] = None,
        custom_fields: Optional[str] = None,
        # V2 specific filters (if applicable, check docs)
        # No specific V2 filters mentioned in migration guide for list other than owner_id/filter_id
    ) -> Dict[str, Any]:
        """
        Returns all organizations. (GET /organizations)

        Args:
            owner_id: If supplied, only organizations owned by the given user will be returned.
            filter_id: ID of the filter to use.
            limit: For pagination, the limit of entries to return.
            cursor: For pagination, the cursor marker from the previous response.
            sort_by: Field to sort by.
            sort_direction: Direction of sorting ('asc', 'desc').
            include_fields: Comma-separated string of optional fields to include.
            custom_fields: Comma-separated string of custom field API keys to include.

        Returns:
            Dictionary containing list of organizations and pagination info.
        """
        params = {
            "user_id": owner_id, # Map owner_id kwarg to user_id param
            "filter_id": filter_id,
            "limit": limit,
            "cursor": cursor,
            "sort_by": sort_by,
            "sort_direction": sort_direction,
            "include_fields": include_fields,
            "custom_fields": custom_fields,
        }
        return self._client._request("GET", "/organizations", params=self._prepare_params(params))

    def create_organization(self, data: Union[Dict[str, Any], OrganizationCreateModel]) -> Dict[str, Any]:
        """
        Creates a new organization. (POST /organizations)

        Args:
            data: Dictionary or OrganizationCreateModel object containing organization details. 'name' is required.

        Returns:
            Dictionary representing the newly created organization.
        """
        if isinstance(data, OrganizationCreateModel):
            payload = data.dict(exclude_unset=True, by_alias=True)
        else:
            payload = data

        if 'name' not in payload or not payload['name']:
             raise ValueError("'name' is required to create an organization.")

        return self._client._request("POST", "/organizations", data=payload)

    def update_organization(
        self, org_id: int, data: Union[Dict[str, Any], OrganizationUpdateModel]
    ) -> Dict[str, Any]:
        """
        Updates an existing organization. (PATCH /organizations/{id})

        Args:
            org_id: The ID of the organization to update.
            data: Dictionary or OrganizationUpdateModel object containing fields to update.

        Returns:
            Dictionary representing the updated organization.
        """
        if isinstance(data, OrganizationUpdateModel):
            payload = data.dict(exclude_unset=True, by_alias=True)
        else:
            payload = data

        return self._client._request("PATCH", f"/organizations/{org_id}", data=payload)

    def delete_organization(self, org_id: int) -> Dict[str, Any]:
        """
        Deletes a specific organization. (DELETE /organizations/{id})
        Note: Migration guide mentions DELETE /api/v{1,2}/organizations (plural), assuming deletion by ID.

        Args:
            org_id: The ID of the organization to delete.

        Returns:
            Dictionary indicating success or failure.
        """
        return self._client._request("DELETE", f"/organizations/{org_id}")