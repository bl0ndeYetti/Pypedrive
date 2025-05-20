from typing import Optional, Dict, Any, Union

from ..client import BaseResource
from ..models.product_variations import ProductVariationCreateModel, ProductVariationUpdateModel

class ProductVariations(BaseResource):
    """
    Encapsulates methods for interacting with the Pipedrive Product Variations V2 API.
    This is a new API in V2.
    Ref: https://pipedrive.readme.io/docs/pipedrive-api-v2-migration-guide#product-variations-api
    """

    def list_variations(self, product_id: int, *, limit: Optional[int] = None, cursor: Optional[str] = None) -> Dict[str, Any]:
        """
        Lists variations for a specific product. (GET /products/{product_id}/variations)
        Note: Docs don't explicitly confirm pagination here, but assume standard cursor/limit.

        Args:
            product_id: The ID of the product whose variations to list.
            limit: For pagination, the limit of entries to return.
            cursor: For pagination, the cursor marker from the previous response.

        Returns:
            Dictionary containing list of product variations and potentially pagination info.
        """
        params = {
            "limit": limit,
            "cursor": cursor,
        }
        # Ensure product_id is included in the path correctly
        path = f"/products/{product_id}/variations"
        return self._client._request("GET", path, params=self._prepare_params(params))

    def create_variation(
        self, product_id: int, data: Union[Dict[str, Any], ProductVariationCreateModel]
    ) -> Dict[str, Any]:
        """
        Creates a new product variation. (POST /products/{product_id}/variations)

        Args:
            product_id: The ID of the product to add a variation to.
            data: Dictionary or ProductVariationCreateModel object containing variation details. 'name' is required.

        Returns:
            Dictionary representing the newly created product variation.
        """
        if isinstance(data, ProductVariationCreateModel):
            payload = data.dict(exclude_unset=True)
        else:
            payload = data

        if 'name' not in payload or not payload['name']:
             raise ValueError("'name' is required to create a product variation.")

        path = f"/products/{product_id}/variations"
        return self._client._request("POST", path, data=payload)

    def update_variation(
        self, product_id: int, variation_id: int, data: Union[Dict[str, Any], ProductVariationUpdateModel]
    ) -> Dict[str, Any]:
        """
        Updates an existing product variation. (PATCH /products/{product_id}/variations/{variation_id})

        Args:
            product_id: The ID of the product containing the variation.
            variation_id: The ID of the variation to update.
            data: Dictionary or ProductVariationUpdateModel object containing fields to update.

        Returns:
            Dictionary representing the updated product variation.
        """
        if isinstance(data, ProductVariationUpdateModel):
            payload = data.dict(exclude_unset=True)
        else:
            payload = data

        path = f"/products/{product_id}/variations/{variation_id}"
        return self._client._request("PATCH", path, data=payload)

    def delete_variation(self, product_id: int, variation_id: int) -> Dict[str, Any]:
        """
        Deletes a specific product variation. (DELETE /products/{product_id}/variations/{variation_id})

        Args:
            product_id: The ID of the product containing the variation.
            variation_id: The ID of the variation to delete.

        Returns:
            Dictionary indicating success or failure.
        """
        path = f"/products/{product_id}/variations/{variation_id}"
        return self._client._request("DELETE", path)