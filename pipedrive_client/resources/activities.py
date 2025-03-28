from typing import Optional, Dict, Any, Union

from ..base import BaseResource
from ..models.activities import ActivityCreateModel, ActivityUpdateModel
# from ..models.common import Address # Import Address if used directly - Removed, only models use it


class Activities(BaseResource):
    """
    Encapsulates methods for interacting with the Pipedrive Activities V2 API.
    Ref: https://pipedrive.readme.io/docs/pipedrive-api-v2-migration-guide#activities-api
    """

    def get_details(self, activity_id: int, *, include_fields: Optional[str] = None) -> Dict[str, Any]:
        """
        Returns details of a specific activity. (GET /activities/{id})

        Args:
            activity_id: The ID of the activity.
            include_fields: Comma-separated string of fields to include (e.g., 'attendees').

        Returns:
            Dictionary representing the activity details.
        """
        params = {"include_fields": include_fields}
        return self._client._request("GET", f"/activities/{activity_id}", params=params) # Pass params directly

    def list_activities(
        self,
        *,
        owner_id: Optional[int] = None, # Renamed from user_id
        filter_id: Optional[int] = None,
        type: Optional[str] = None,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        start_date: Optional[str] = None, # YYYY-MM-DD
        end_date: Optional[str] = None,   # YYYY-MM-DD
        done: Optional[bool] = None,      # Use True/False
        sort_by: Optional[str] = None,    # e.g., 'due_date', 'add_time'
        sort_direction: Optional[str] = None, # 'asc' or 'desc'
        include_fields: Optional[str] = None, # e.g., 'attendees'
        # V2 Specific Filters (if applicable, check docs)
        deal_id: Optional[int] = None,
        person_id: Optional[int] = None,
        org_id: Optional[int] = None,
        project_id: Optional[int] = None,
        lead_id: Optional[int] = None,
    ) -> Dict[str, Any]:
        """
        Returns all activities. (GET /activities)

        Args:
            owner_id: If supplied, only activities owned by the given user will be returned.
            filter_id: ID of the filter to use.
            type: Type of the activity (e.g., 'call', 'meeting').
            limit: For pagination, the limit of entries to return.
            cursor: For pagination, the cursor marker from the previous response.
            start_date: Date YYYY-MM-DD. Start of the period.
            end_date: Date YYYY-MM-DD. End of the period.
            done: Whether the activity is done or not (True or False).
            sort_by: Field to sort by (e.g., 'due_date', 'add_time', 'update_time').
            sort_direction: Direction of sorting ('asc', 'desc').
            include_fields: Comma-separated string of fields to include (e.g., 'attendees').
            deal_id: Filter by associated Deal ID.
            person_id: Filter by associated Person ID.
            org_id: Filter by associated Organization ID.
            project_id: Filter by associated Project ID.
            lead_id: Filter by associated Lead ID.

        Returns:
            Dictionary containing list of activities and pagination info.
        """
        params = {
            "user_id": owner_id, # Map owner_id kwarg to user_id param
            "filter_id": filter_id,
            "type": type,
            "limit": limit,
            "cursor": cursor,
            "start_date": start_date,
            "end_date": end_date,
            "done": done,
            "sort_by": sort_by,
            "sort_direction": sort_direction,
            "include_fields": include_fields,
            "deal_id": deal_id,
            "person_id": person_id,
            "org_id": org_id,
            project_id: project_id,
            lead_id: lead_id,
        }
        return self._client._request("GET", "/activities", params=params) # Pass params directly

    def create_activity(self, data: Union[Dict[str, Any], ActivityCreateModel]) -> Dict[str, Any]:
        """
        Creates a new activity. (POST /activities)

        Args:
            data: Dictionary or ActivityCreateModel object containing activity details.
                  'subject' is required.
                  Use 'participants' list to set person_id indirectly: [{"person_id": 123, "primary": True}]

        Returns:
            Dictionary representing the newly created activity.
        """
        if isinstance(data, ActivityCreateModel):
            payload = data.dict(exclude_unset=True, by_alias=True)
        else:
            payload = data

        # Ensure person_id is not directly set if participants are used
        if 'participants' in payload and payload.get('participants'):
            payload.pop('person_id', None)

        return self._client._request("POST", "/activities", data=payload)

    def update_activity(
        self, activity_id: int, data: Union[Dict[str, Any], ActivityUpdateModel]
    ) -> Dict[str, Any]:
        """
        Updates an existing activity. (PATCH /activities/{id})

        Args:
            activity_id: The ID of the activity to update.
            data: Dictionary or ActivityUpdateModel object containing fields to update.
                  Use 'participants' list to update person_id indirectly.

        Returns:
            Dictionary representing the updated activity.
        """
        if isinstance(data, ActivityUpdateModel):
            payload = data.dict(exclude_unset=True, by_alias=True)
        else:
            payload = data

        # Ensure person_id is not directly set if participants are used
        if 'participants' in payload and payload.get('participants'):
            payload.pop('person_id', None)

        return self._client._request("PATCH", f"/activities/{activity_id}", data=payload)

    def delete_activity(self, activity_id: int) -> Dict[str, Any]:
        """
        Deletes a specific activity. (DELETE /activities/{id})
        Note: Migration guide mentions DELETE /api/v{1,2}/activities (plural), but standard REST is by ID.
              Assuming deletion by ID.

        Args:
            activity_id: The ID of the activity to delete.

        Returns:
            Dictionary indicating success or failure.
        """
        return self._client._request("DELETE", f"/activities/{activity_id}")