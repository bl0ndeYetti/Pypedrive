from typing import Optional, Dict, Any, Union, List

from ..client import BaseResource
from ..models.products import ProductCreateModel, ProductUpdateModel


class Products(BaseResource):
    """
    Encapsulates methods for interacting with the Pipedrive Products V2 API.
    Ref: https://pipedrive.readme.io/docs/pipedrive-api-v2-migration-guide#products-api
    """

    def get_details(self, product_id: int) -> Dict[str, Any]:
        """
        Returns details of a specific product. (GET /products/{id})
        V2 has no specific extra params mentioned like include_fields/custom_fields for GET by ID.

        Args:
            product_id: The ID of the product.

        Returns:
            Dictionary representing the product details.
        """
        return self._client._request("GET", f"/products/{product_id}")

    def list_products(
        self,
        *,
        owner_id: Optional[int] = None, # Renamed from user_id
        # filter_id: Optional[int] = None, # Not mentioned for v2 products list
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        sort_by: Optional[str] = None, # 'id', 'add_time', 'update_time', 'name'
        sort_direction: Optional[str] = None, # 'asc', 'desc'
        # V1 params 'get_summary', 'first_char' are removed
    ) -> Dict[str, Any]:
        """
        Returns all products. (GET /products)

        Args:
            owner_id: If supplied, only products owned by the given user will be returned.
            limit: For pagination, the limit of entries to return.
            cursor: For pagination, the cursor marker from the previous response.
            sort_by: Field to sort by ('id', 'add_time', 'update_time', 'name').
            sort_direction: Direction of sorting ('asc', 'desc').

        Returns:
            Dictionary containing list of products and pagination info.
        """
        params = {
            "user_id": owner_id, # Map owner_id kwarg to user_id param
            "limit": limit,
            "cursor": cursor,
            "sort_by": sort_by,
            "sort_direction": sort_direction,
        }
        return self._client._request("GET", "/products", params=self._prepare_params(params))

    def create_product(self, data: Union[Dict[str, Any], ProductCreateModel]) -> Dict[str, Any]:
        """
        Creates a new product. (POST /products)

        Args:
            data: Dictionary or ProductCreateModel object containing product details. 'name' is required.

        Returns:
            Dictionary representing the newly created product.
        """
        if isinstance(data, ProductCreateModel):
            payload = data.dict(exclude_unset=True, by_alias=True)
        else:
            payload = data

        if 'name' not in payload or not payload['name']:
             raise ValueError("'name' is required to create a product.")

        return self._client._request("POST", "/products", data=payload)

    def update_product(self, product_id: int, data: Union[Dict[str, Any], ProductUpdateModel]) -> Dict[str, Any]:
        """
        Updates an existing product. (PATCH /products/{id})

        Args:
            product_id: The ID of the product to update.
            data: Dictionary or ProductUpdateModel object containing fields to update.
                  Note: Updating 'prices' replaces the entire array.

        Returns:
            Dictionary representing the updated product.
        """
        if isinstance(data, ProductUpdateModel):
            payload = data.dict(exclude_unset=True, by_alias=True)
        else:
            payload = data

        return self._client._request("PATCH", f"/products/{product_id}", data=payload)

    def delete_product(self, product_id: int) -> Dict[str, Any]:
        """
        Deletes a specific product. (DELETE /products/{id})
        Note: Migration guide mentions DELETE /api/v{1,2}/products (plural), assuming deletion by ID.

        Args:
            product_id: The ID of the product to delete.

        Returns:
            Dictionary indicating success or failure.
        """
        return self._client._request("DELETE", f"/products/{product_id}")