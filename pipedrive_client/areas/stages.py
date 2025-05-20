from typing import Optional, Dict, Any, Union

from ..client import BaseResource
from ..models.stages import StageCreateModel, StageUpdateModel


class Stages(BaseResource):
    """
    Encapsulates methods for interacting with the Pipedrive Stages V2 API.
    Ref: https://pipedrive.readme.io/docs/pipedrive-api-v2-migration-guide#stages-api
    """

    def get_details(self, stage_id: int) -> Dict[str, Any]:
        """
        Returns details of a specific stage. (GET /stages/{id})

        Args:
            stage_id: The ID of the stage.

        Returns:
            Dictionary representing the stage details.
        """
        return self._client._request("GET", f"/stages/{stage_id}")

    def list_stages(
        self,
        *,
        pipeline_id: Optional[int] = None,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        # sort_by/sort_direction not explicitly mentioned, assume not supported unless verified
    ) -> Dict[str, Any]:
        """
        Returns all stages, optionally filtered by pipeline. (GET /stages)
        Note: Docs don't explicitly confirm pagination, but assume standard cursor/limit.

        Args:
            pipeline_id: ID of the pipeline to filter stages by. If omitted, returns stages from all pipelines.
            limit: For pagination, the limit of entries to return.
            cursor: For pagination, the cursor marker from the previous response.

        Returns:
            Dictionary containing list of stages and pagination info.
        """
        params = {
            "pipeline_id": pipeline_id,
            "limit": limit,
            "cursor": cursor,
        }
        return self._client._request("GET", "/stages", params=self._prepare_params(params))

    def create_stage(self, data: Union[Dict[str, Any], StageCreateModel]) -> Dict[str, Any]:
        """
        Creates a new stage. (POST /stages)

        Args:
            data: Dictionary or StageCreateModel object containing stage details. 'name' and 'pipeline_id' are required.

        Returns:
            Dictionary representing the newly created stage.
        """
        if isinstance(data, StageCreateModel):
            payload = data.dict(exclude_unset=True, by_alias=True)
        else:
            payload = data

        if 'name' not in payload or not payload['name']:
             raise ValueError("'name' is required to create a stage.")
        if 'pipeline_id' not in payload or payload['pipeline_id'] is None:
             raise ValueError("'pipeline_id' is required to create a stage.")

        return self._client._request("POST", "/stages", data=payload)

    def update_stage(self, stage_id: int, data: Union[Dict[str, Any], StageUpdateModel]) -> Dict[str, Any]:
        """
        Updates an existing stage. (PATCH /stages/{id})

        Args:
            stage_id: The ID of the stage to update.
            data: Dictionary or StageUpdateModel object containing fields to update.

        Returns:
            Dictionary representing the updated stage.
        """
        if isinstance(data, StageUpdateModel):
            payload = data.dict(exclude_unset=True, by_alias=True)
        else:
            payload = data

        return self._client._request("PATCH", f"/stages/{stage_id}", data=payload)

    def delete_stage(self, stage_id: int) -> Dict[str, Any]:
        """
        Deletes a specific stage. (DELETE /stages/{id})
        Note: Migration guide mentions DELETE /api/v{1,2}/stages (plural), assuming deletion by ID.

        Args:
            stage_id: The ID of the stage to delete.

        Returns:
            Dictionary indicating success or failure.
        """
        return self._client._request("DELETE", f"/stages/{stage_id}")