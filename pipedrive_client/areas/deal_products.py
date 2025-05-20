from typing import Optional, Dict, Any, Union, List

from ..client import BaseResource
from ..models.deal_products import DealProductAttachModel, DealProductUpdateModel


class DealProducts(BaseResource):
    """
    Encapsulates methods for interacting with the Pipedrive Deal Products V2 API.
    Ref: https://pipedrive.readme.io/docs/pipedrive-api-v2-migration-guide#deal-products-api
    """

    def list_deal_products(self, deal_id: int, *, limit: Optional[int] = None, cursor: Optional[str] = None) -> Dict[str, Any]:
        """
        Lists products attached to a specific deal. (GET /deals/{id}/products)

        Args:
            deal_id: The ID of the deal.
            limit: For pagination, the limit of entries to return.
            cursor: For pagination, the cursor marker from the previous response.

        Returns:
            Dictionary containing list of deal products and pagination info.
        """
        params = {
            "limit": limit,
            "cursor": cursor,
        }
        return self._client._request("GET", f"/deals/{deal_id}/products", params=self._prepare_params(params))

    def list_products_for_deals(self, deal_ids: Union[List[int], str], *, limit: Optional[int] = None, cursor: Optional[str] = None) -> Dict[str, Any]:
        """
        Lists products attached to multiple deals. (GET /deals/products)

        Args:
            deal_ids: Comma-separated string or list of deal IDs (up to 100).
            limit: For pagination, the limit of entries to return.
            cursor: For pagination, the cursor marker from the previous response.

        Returns:
            Dictionary containing list of deal products and pagination info.
        """
        if isinstance(deal_ids, list):
            if len(deal_ids) > 100:
                raise ValueError("Cannot request products for more than 100 deals at once.")
            deal_ids_str = ','.join(map(str, deal_ids))
        else:
            deal_ids_str = deal_ids # Assume it's already a comma-separated string

        params = {
            "deal_ids": deal_ids_str,
            "limit": limit,
            "cursor": cursor,
        }
        return self._client._request("GET", "/deals/products", params=self._prepare_params(params))

    def attach_product_to_deal(
        self, deal_id: int, data: Union[Dict[str, Any], DealProductAttachModel]
    ) -> Dict[str, Any]:
        """
        Attaches a product to a deal. (POST /deals/{id}/products)

        Args:
            deal_id: The ID of the deal.
            data: Dictionary or DealProductAttachModel object containing attachment details.
                  Requires 'product_id', 'item_price', 'quantity'.

        Returns:
            Dictionary representing the newly created deal-product attachment.
        """
        if isinstance(data, DealProductAttachModel):
            payload = data.dict(exclude_unset=True, by_alias=True)
        else:
            payload = data

        if not all(k in payload for k in ['product_id', 'item_price', 'quantity']):
             raise ValueError("'product_id', 'item_price', and 'quantity' are required.")

        return self._client._request("POST", f"/deals/{deal_id}/products", data=payload)

    def update_deal_product(
        self, deal_id: int, product_attachment_id: int, data: Union[Dict[str, Any], DealProductUpdateModel]
    ) -> Dict[str, Any]:
        """
        Updates a product attachment on a deal. (PATCH /deals/{id}/products/{product_attachment_id})

        Args:
            deal_id: The ID of the deal.
            product_attachment_id: The ID of the deal-product attachment record.
            data: Dictionary or DealProductUpdateModel object containing fields to update.

        Returns:
            Dictionary representing the updated deal-product attachment.
        """
        if isinstance(data, DealProductUpdateModel):
            payload = data.dict(exclude_unset=True, by_alias=True)
        else:
            payload = data

        return self._client._request(
            "PATCH",
            f"/deals/{deal_id}/products/{product_attachment_id}",
            data=payload
        )

    def delete_deal_product(self, deal_id: int, product_attachment_id: int) -> Dict[str, Any]:
        """
        Deletes a specific product attachment from a deal. (DELETE /deals/{id}/products/{product_attachment_id})

        Args:
            deal_id: The ID of the deal.
            product_attachment_id: The ID of the deal-product attachment record to delete.

        Returns:
            Dictionary indicating success or failure.
        """
        return self._client._request(
            "DELETE",
            f"/deals/{deal_id}/products/{product_attachment_id}"
        )

    def delete_all_deal_products(self, deal_id: int) -> Dict[str, Any]:
        """
        Deletes all product attachments from a deal. (DELETE /deals/{id}/products)
        Based on the V2 migration guide description for DELETE /api/v1/deals/:id/products.

        Args:
            deal_id: The ID of the deal from which to delete all products.

        Returns:
            Dictionary indicating success or failure.
        """
        return self._client._request("DELETE", f"/deals/{deal_id}/products")