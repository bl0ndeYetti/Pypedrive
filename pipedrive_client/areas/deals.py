from typing import Optional, Dict, Any, Union, List

from ..base import BaseResource
# from ..exceptions import PipedriveAPIError # Removed unused import
from ..models.deals import (
    DealCreateModel,
    DealUpdateModel,
    DealStatusEnum,
    SortDirectionEnum,
)


class Deals(BaseResource):
    """
    Encapsulates methods for interacting with the Pipedrive Deals V2 API.
    Ref: https://pipedrive.readme.io/docs/pipedrive-api-v2-migration-guide#deals-api
    """

    def get_details(
        self, deal_id: int, *, include_fields: Optional[str] = None, custom_fields: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Returns details of a specific deal. (GET /deals/{id})

        Args:
            deal_id: The ID of the deal.
            include_fields: Comma-separated string of optional fields to include (e.g., 'next_activity_id,files_count').
            custom_fields: Comma-separated string of custom field API keys to include.

        Returns:
            Dictionary representing the deal details.
        """
        params = {
            "include_fields": include_fields,
            "custom_fields": custom_fields,
        }
        return self._client._request(
            "GET",
            f"deals/{deal_id}",
            params=self._prepare_params(params),
        )

    def list_deals(
        self,
        *,
        owner_id: Optional[int] = None,
        filter_id: Optional[int] = None,
        stage_id: Optional[int] = None,
        pipeline_id: Optional[int] = None,
        status: Optional[DealStatusEnum] = None,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        sort_by: Optional[str] = None,
        sort_direction: Optional[SortDirectionEnum] = None,
        person_id: Optional[int] = None,
        org_id: Optional[int] = None,
        include_fields: Optional[str] = None,
        custom_fields: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Returns all deals. (GET /deals)
        """
        params = {
            "user_id": owner_id,
            "filter_id": filter_id,
            "stage_id": stage_id,
            "pipeline_id": pipeline_id,
            "status": status,
            "limit": limit,
            "cursor": cursor,
            "sort_by": sort_by,
            "sort_direction": sort_direction,
            "person_id": person_id,
            "org_id": org_id,
            "include_fields": include_fields,
            "custom_fields": custom_fields,
        }
        return self._client._request(
            "GET",
            "deals",
            params=self._prepare_params(params),
        )

    def create_deal(self, data: Union[Dict[str, Any], DealCreateModel]) -> Dict[str, Any]:
        """Creates a new deal. (POST /deals)"""
        if isinstance(data, DealCreateModel):
            payload = data.dict(exclude_unset=True, by_alias=True)
        else:
            payload = data

        if 'title' not in payload or not payload['title']:
             raise ValueError("'title' is required to create a deal.")

        return self._client._request("POST", "deals", data=payload)

    def update_deal(self, deal_id: int, data: Union[Dict[str, Any], DealUpdateModel]) -> Dict[str, Any]:
        """Updates an existing deal. (PATCH /deals/{id})"""
        if isinstance(data, DealUpdateModel):
            payload = data.dict(exclude_unset=True, by_alias=True)
        else:
            payload = data

        return self._client._request("PATCH", f"deals/{deal_id}", data=payload)

    def delete_deal(self, deal_id: int) -> Dict[str, Any]:
        """Deletes a specific deal. (DELETE /deals/{id})"""
        return self._client._request("DELETE", f"deals/{deal_id}")
    
    def search_deals(
        self,
        term: str,
        *,
        fields: Optional[str] = None,
        exact_match: Optional[bool] = None,
        person_id: Optional[int] = None,
        organization_id: Optional[int] = None,
        status: Optional[DealStatusEnum] = None,
        include_fields: Optional[str] = None,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Search for deals. (GET /deals/search)"""
        params = {
            "term": term,
            "fields": fields,
            "exact_match": exact_match,
            "person_id": person_id,
            "organization_id": organization_id,
            "status": status,
            "include_fields": include_fields,
            "limit": limit,
            "cursor": cursor,
        }
        return self._client._request(
            "GET",
            "deals/search",
            params=self._prepare_params(params),
        )
    