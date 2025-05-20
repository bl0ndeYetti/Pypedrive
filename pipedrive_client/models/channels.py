from typing import Optional, List
from pydantic import BaseModel, Field


class AddChannelBody(BaseModel):
    """Body parameters for POST /v1/channels."""

    name: str = Field(..., description="The name of the channel")
    provider_channel_id: str = Field(..., description="The channel ID")
    avatar_url: Optional[str] = Field(
        None, description="URL for an icon that represents the channel"
    )
    template_support: Optional[bool] = Field(
        None,
        description="Enable templates logic on UI if true"
    )
    provider_type: Optional[str] = Field(
        "other",
        description="Controls icons associated with the channel"
    )


class Channel(BaseModel):
    """Channel object returned by the API."""

    id: str = Field(..., description="Unique channel ID")
    name: str = Field(..., description="The name of the channel")
    avatar_url: Optional[str] = Field(
        None, description="URL for an icon that represents the channel"
    )
    provider_channel_id: str = Field(
        ..., description="The channel ID specified when creating the channel"
    )
    marketplace_client_id: Optional[str] = Field(
        None, description="Client ID of the app in Pipedrive marketplace"
    )
    pd_company_id: Optional[int] = Field(
        None, description="ID of the user's company in Pipedrive"
    )
    pd_user_id: Optional[int] = Field(None, description="ID of the user in Pipedrive")
    created_at: Optional[str] = Field(
        None, description="Date and time when the channel was created"
    )
    provider_type: Optional[str] = Field(None, description="Provider type value")
    template_support: Optional[bool] = Field(
        None, description="Value of template_support sent to this endpoint"
    )


class MessageAttachment(BaseModel):
    """Attachment information used in messages."""

    id: str = Field(..., description="Attachment ID")
    type: str = Field(..., description="Mime-type of the attachment")
    url: str = Field(..., description="URL to the file")
    name: Optional[str] = Field(None, description="Name of the attachment")
    size: Optional[float] = Field(None, description="Size of the attachment")
    preview_url: Optional[str] = Field(
        None, description="URL to a preview picture of the file"
    )
    link_expires: Optional[bool] = Field(
        False,
        description="Whether the link expires and should be refreshed"
    )


class ReceiveMessageBody(BaseModel):
    """Body parameters for POST /v1/channels/messages/receive."""

    id: str = Field(..., description="ID of the message")
    channel_id: str = Field(..., description="Channel ID in the provider")
    sender_id: str = Field(..., description="ID of the provider's user that sent the message")
    conversation_id: str = Field(..., description="ID of the conversation")
    message: str = Field(..., description="Body of the message")
    status: str = Field(..., description="Status of the message")
    created_at: str = Field(..., description="When the message was created in UTC")
    reply_by: Optional[str] = Field(
        None, description="When the message can no longer receive a reply"
    )
    conversation_link: Optional[str] = Field(
        None, description="URL that opens the conversation on provider side"
    )
    attachments: Optional[List[MessageAttachment]] = Field(
        None, description="List of attachments in the message"
    )

