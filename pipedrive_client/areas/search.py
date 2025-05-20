from typing import Optional, Dict, Any, List, Union

from ..base import BaseResource

class Search(BaseResource):
    """
    Encapsulates methods for interacting with the Pipedrive Search V2 API.
    Ref: https://pipedrive.readme.io/docs/pipedrive-api-v2-migration-guide#search-api
    """

    def _search_resource(
        self,
        resource_path: str,
        term: str,
        *,
        fields: Optional[str] = None, # Comma-separated
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        sort_by: Optional[str] = None, # Support varies, check docs
        sort_direction: Optional[str] = None, # Support varies
        # V2 introduces exact_match=True equivalent in itemSearch/field, not here
        # V1 exact_match param is removed here
    ) -> Dict[str, Any]:
        """Helper for resource-specific searches."""
        params = {
            "term": term,
            "fields": fields,
            "limit": limit,
            "cursor": cursor,
            "sort_by": sort_by,
            "sort_direction": sort_direction,
        }
        return self._client._request("GET", resource_path, params=self._prepare_params(params))

    def search_deals(self, term: str, *, fields: Optional[str] = None, limit: Optional[int] = None, cursor: Optional[str] = None, sort_by: Optional[str] = None, sort_direction: Optional[str] = None) -> Dict[str, Any]:
        """Searches deals. (GET /deals/search)"""
        return self._search_resource("/deals/search", term, fields=fields, limit=limit, cursor=cursor, sort_by=sort_by, sort_direction=sort_direction)

    def search_persons(self, term: str, *, fields: Optional[str] = None, limit: Optional[int] = None, cursor: Optional[str] = None, sort_by: Optional[str] = None, sort_direction: Optional[str] = None) -> Dict[str, Any]:
        """Searches persons. (GET /persons/search)"""
        return self._search_resource("/persons/search", term, fields=fields, limit=limit, cursor=cursor, sort_by=sort_by, sort_direction=sort_direction)

    def search_organizations(self, term: str, *, fields: Optional[str] = None, limit: Optional[int] = None, cursor: Optional[str] = None, sort_by: Optional[str] = None, sort_direction: Optional[str] = None) -> Dict[str, Any]:
        """Searches organizations. (GET /organizations/search)"""
        return self._search_resource("/organizations/search", term, fields=fields, limit=limit, cursor=cursor, sort_by=sort_by, sort_direction=sort_direction)

    def search_leads(self, term: str, *, fields: Optional[str] = None, limit: Optional[int] = None, cursor: Optional[str] = None, sort_by: Optional[str] = None, sort_direction: Optional[str] = None) -> Dict[str, Any]:
        """Searches leads. (GET /leads/search)"""
        # Note: Leads API itself might not be fully V2 yet, but search endpoint is mentioned.
        return self._search_resource("/leads/search", term, fields=fields, limit=limit, cursor=cursor, sort_by=sort_by, sort_direction=sort_direction)

    def search_products(self, term: str, *, fields: Optional[str] = None, limit: Optional[int] = None, cursor: Optional[str] = None, sort_by: Optional[str] = None, sort_direction: Optional[str] = None) -> Dict[str, Any]:
        """Searches products. (GET /products/search)"""
        return self._search_resource("/products/search", term, fields=fields, limit=limit, cursor=cursor, sort_by=sort_by, sort_direction=sort_direction)

    def search_items(
        self,
        term: str,
        *,
        item_types: Optional[str] = None, # Comma-separated: 'deal', 'person', 'organization', 'product', 'lead', 'project'
        fields: Optional[str] = None,     # Comma-separated
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        # V1 'start' removed, uses cursor/limit now
    ) -> Dict[str, Any]:
        """
        Searches across multiple item types. (GET /itemSearch)

        Args:
            term: The search term.
            item_types: Comma-separated list of item types to search (e.g., 'deal,person').
            fields: Comma-separated list of fields to search within.
            limit: For pagination.
            cursor: For pagination.

        Returns:
            Search results.
        """
        params = {
            "term": term,
            "item_types": item_types,
            "fields": fields,
            "limit": limit,
            "cursor": cursor,
        }
        return self._client._request("GET", "/itemSearch", params=self._prepare_params(params))

    def search_items_by_field(
        self,
        term: str,
        field: str, # Renamed from field_key
        entity_type: str, # Renamed from field_type, values: 'deal', 'lead', 'person', 'organization', 'product', 'project'
        *,
        match: Optional[str] = None, # 'exact', 'beginning', 'middle' (replaces exact_match boolean)
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        # V1 'return_item_ids' removed (always included now)
    ) -> Dict[str, Any]:
        """
        Searches for items by the value of a specific field. (GET /itemSearch/field)

        Args:
            term: The value to search for.
            field: The API key of the field to search within (renamed from field_key).
            entity_type: The type of entity to search ('deal', 'lead', 'person', 'organization', 'product', 'project').
            match: Type of matching ('exact', 'beginning', 'middle'). Defaults to server-side default (likely 'middle').
            limit: For pagination.
            cursor: For pagination.

        Returns:
            Search results.
        """
        params = {
            "term": term,
            "field": field,
            "entity_type": entity_type,
            "match": match,
            "limit": limit,
            "cursor": cursor,
        }
        return self._client._request("GET", "/itemSearch/field", params=self._prepare_params(params))