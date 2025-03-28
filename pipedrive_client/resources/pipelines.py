from typing import Optional, Dict, Any, Union

from ..client import BaseResource
from ..models.pipelines import PipelineCreateModel, PipelineUpdateModel


class Pipelines(BaseResource):
    """
    Encapsulates methods for interacting with the Pipedrive Pipelines V2 API.
    Ref: https://pipedrive.readme.io/docs/pipedrive-api-v2-migration-guide#pipelines-api
    """

    def get_details(self, pipeline_id: int) -> Dict[str, Any]:
        """
        Returns details of a specific pipeline. (GET /pipelines/{id})

        Args:
            pipeline_id: The ID of the pipeline.

        Returns:
            Dictionary representing the pipeline details.
        """
        return self._client._request("GET", f"/pipelines/{pipeline_id}")

    def list_pipelines(self, *, limit: Optional[int] = None, cursor: Optional[str] = None) -> Dict[str, Any]:
        """
        Returns all pipelines. (GET /pipelines)
        Note: Docs don't explicitly confirm pagination/sorting here, but assume standard cursor/limit.

        Args:
            limit: For pagination, the limit of entries to return.
            cursor: For pagination, the cursor marker from the previous response.

        Returns:
            Dictionary containing list of pipelines and pagination info.
        """
        params = {
            "limit": limit,
            "cursor": cursor,
        }
        return self._client._request("GET", "/pipelines", params=self._prepare_params(params))

    def create_pipeline(self, data: Union[Dict[str, Any], PipelineCreateModel]) -> Dict[str, Any]:
        """
        Creates a new pipeline. (POST /pipelines)

        Args:
            data: Dictionary or PipelineCreateModel object containing pipeline details. 'name' is required.
                  'order_nr' is read-only in V2.

        Returns:
            Dictionary representing the newly created pipeline.
        """
        if isinstance(data, PipelineCreateModel):
            payload = data.dict(exclude_unset=True, by_alias=True)
        else:
            payload = data

        if 'name' not in payload or not payload['name']:
             raise ValueError("'name' is required to create a pipeline.")

        payload.pop('order_nr', None) # Ensure order_nr is not sent

        return self._client._request("POST", "/pipelines", data=payload)

    def update_pipeline(self, pipeline_id: int, data: Union[Dict[str, Any], PipelineUpdateModel]) -> Dict[str, Any]:
        """
        Updates an existing pipeline. (PATCH /pipelines/{id})

        Args:
            pipeline_id: The ID of the pipeline to update.
            data: Dictionary or PipelineUpdateModel object containing fields to update.
                  'order_nr' is read-only in V2.

        Returns:
            Dictionary representing the updated pipeline.
        """
        if isinstance(data, PipelineUpdateModel):
            payload = data.dict(exclude_unset=True, by_alias=True)
        else:
            payload = data

        payload.pop('order_nr', None) # Ensure order_nr is not sent

        return self._client._request("PATCH", f"/pipelines/{pipeline_id}", data=payload)

    def delete_pipeline(self, pipeline_id: int) -> Dict[str, Any]:
        """
        Deletes a specific pipeline. (DELETE /pipelines/{id})
        Note: Migration guide mentions DELETE /api/v{1,2}/pipelines (plural), assuming deletion by ID.

        Args:
            pipeline_id: The ID of the pipeline to delete.

        Returns:
            Dictionary indicating success or failure.
        """
        return self._client._request("DELETE", f"/pipelines/{pipeline_id}")