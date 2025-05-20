from typing import Optional
from pydantic import BaseModel, Field

class GetFilesParams(BaseModel):
    """Query parameters for GET /v1/files"""

    start: Optional[int] = Field(
        None, description="Pagination start offset"
    )
    limit: Optional[int] = Field(
        None,
        description="Items shown per page (max 100)"
    )
    sort: Optional[str] = Field(
        None,
        description="Sort field, supported: 'id', 'update_time'"
    )

class AddFileBody(BaseModel):
    """Body parameters for POST /v1/files"""

    file: bytes = Field(..., description="Binary file contents")
    deal_id: Optional[int] = Field(
        None, description="Deal ID to associate file with"
    )
    person_id: Optional[int] = Field(
        None, description="Person ID to associate file with"
    )
    org_id: Optional[int] = Field(
        None, description="Organization ID to associate file with"
    )
    product_id: Optional[int] = Field(
        None, description="Product ID to associate file with"
    )
    activity_id: Optional[int] = Field(
        None, description="Activity ID to associate file with"
    )
    lead_id: Optional[str] = Field(
        None, description="Lead ID to associate file with"
    )

class RemoteFileCreateBody(BaseModel):
    """Body parameters for POST /v1/files/remote"""

    file_type: str = Field(..., description="Remote file type, e.g. 'gdoc'")
    title: str = Field(..., description="Title of the remote file")
    item_type: str = Field(..., description="Item type to link the file to")
    item_id: int = Field(..., description="ID of the item to link the file to")
    remote_location: str = Field(
        ..., description="Remote location type, currently only 'googledrive'"
    )

class RemoteFileLinkBody(BaseModel):
    """Body parameters for POST /v1/files/remoteLink"""

    item_type: str = Field(..., description="Item type to link the file to")
    item_id: int = Field(..., description="ID of the item to link the file to")
    remote_id: str = Field(..., description="Remote item identifier")
    remote_location: str = Field(
        ..., description="Remote location type, currently only 'googledrive'"
    )

class FileUpdateBody(BaseModel):
    """Body parameters for PUT /v1/files/{id}"""

    name: Optional[str] = Field(None, description="Visible name of the file")
    description: Optional[str] = Field(
        None, description="Description of the file"
    )
