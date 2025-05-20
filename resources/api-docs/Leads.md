---
url: "https://developers.pipedrive.com/docs/api/v1/Leads"
title: "Pipedrive API Reference and Documentation"
---

API Reference

###### API Reference

[Getting started](https://developers.pipedrive.com/docs/api/v1)

###### Endpoints

[Activities](https://developers.pipedrive.com/docs/api/v1/Activities)

[ActivityFields](https://developers.pipedrive.com/docs/api/v1/ActivityFields)

[ActivityTypes](https://developers.pipedrive.com/docs/api/v1/ActivityTypes)

[Billing](https://developers.pipedrive.com/docs/api/v1/Billing)

[CallLogs](https://developers.pipedrive.com/docs/api/v1/CallLogs)

[Channels](https://developers.pipedrive.com/docs/api/v1/Channels)

[Currencies](https://developers.pipedrive.com/docs/api/v1/Currencies)

[Deals](https://developers.pipedrive.com/docs/api/v1/Deals)

[DealFields](https://developers.pipedrive.com/docs/api/v1/DealFields)

[Files](https://developers.pipedrive.com/docs/api/v1/Files)

[Filters](https://developers.pipedrive.com/docs/api/v1/Filters)

[Goals](https://developers.pipedrive.com/docs/api/v1/Goals)

[ItemSearch](https://developers.pipedrive.com/docs/api/v1/ItemSearch)

[Leads](https://developers.pipedrive.com/docs/api/v1/Leads)

[GET\\
\\
Get all leads](https://developers.pipedrive.com/docs/api/v1/Leads#getLeads)

[GET\\
\\
Get all archived leads](https://developers.pipedrive.com/docs/api/v1/Leads#getArchivedLeads)

[GET\\
\\
Get one lead](https://developers.pipedrive.com/docs/api/v1/Leads#getLead)

[GET\\
\\
List permitted users](https://developers.pipedrive.com/docs/api/v1/Leads#getLeadUsers)

[GET\\
\\
Search leads](https://developers.pipedrive.com/docs/api/v1/Leads#searchLeads)

[GET\\
\\
Get Lead conversion status (BETA)](https://developers.pipedrive.com/docs/api/v1/Leads#getLeadConversionStatus)

[POST\\
\\
Add a lead](https://developers.pipedrive.com/docs/api/v1/Leads#addLead)

[POST\\
\\
Convert a lead to a deal (BETA)](https://developers.pipedrive.com/docs/api/v1/Leads#convertLeadToDeal)

[PATCH\\
\\
Update a lead](https://developers.pipedrive.com/docs/api/v1/Leads#updateLead)

[DELETE\\
\\
Delete a lead](https://developers.pipedrive.com/docs/api/v1/Leads#deleteLead)

[LeadLabels](https://developers.pipedrive.com/docs/api/v1/LeadLabels)

[LeadSources](https://developers.pipedrive.com/docs/api/v1/LeadSources)

[LegacyTeams](https://developers.pipedrive.com/docs/api/v1/LegacyTeams)

[Mailbox](https://developers.pipedrive.com/docs/api/v1/Mailbox)

[Meetings](https://developers.pipedrive.com/docs/api/v1/Meetings)

[Notes](https://developers.pipedrive.com/docs/api/v1/Notes)

[NoteFields](https://developers.pipedrive.com/docs/api/v1/NoteFields)

[OAuth 2.0](https://developers.pipedrive.com/docs/api/v1/Oauth)

[Organizations](https://developers.pipedrive.com/docs/api/v1/Organizations)

[OrganizationFields](https://developers.pipedrive.com/docs/api/v1/OrganizationFields)

[OrganizationRelationships](https://developers.pipedrive.com/docs/api/v1/OrganizationRelationships)

[PermissionSets](https://developers.pipedrive.com/docs/api/v1/PermissionSets)

[Persons](https://developers.pipedrive.com/docs/api/v1/Persons)

[PersonFields](https://developers.pipedrive.com/docs/api/v1/PersonFields)

[Pipelines](https://developers.pipedrive.com/docs/api/v1/Pipelines)

[Products](https://developers.pipedrive.com/docs/api/v1/Products)

[ProductFields](https://developers.pipedrive.com/docs/api/v1/ProductFields)

[Projects](https://developers.pipedrive.com/docs/api/v1/Projects)

[ProjectTemplates](https://developers.pipedrive.com/docs/api/v1/ProjectTemplates)

[Recents](https://developers.pipedrive.com/docs/api/v1/Recents)

[Roles](https://developers.pipedrive.com/docs/api/v1/Roles)

[Stages](https://developers.pipedrive.com/docs/api/v1/Stages)

[Subscriptions](https://developers.pipedrive.com/docs/api/v1/Subscriptions)

[Tasks](https://developers.pipedrive.com/docs/api/v1/Tasks)

[Users](https://developers.pipedrive.com/docs/api/v1/Users)

[UserConnections](https://developers.pipedrive.com/docs/api/v1/UserConnections)

[UserSettings](https://developers.pipedrive.com/docs/api/v1/UserSettings)

[Webhooks](https://developers.pipedrive.com/docs/api/v1/Webhooks)

## Leads

Run in Postman

Leads are potential deals stored in Leads Inbox before they are archived or converted to a deal. Each lead needs to be named (using the `title` field) and be linked to a person or an organization. In addition to that, a lead can contain most of the fields a deal can (such as `value` or `expected_close_date`).

#### Get all leads

![Copy link](<Base64-Image-Removed>)

Returns multiple not archived leads. Leads are sorted by the time they were created, from oldest to newest. Pagination can be controlled using `limit` and `start` query parameters. If a lead contains custom fields, the fields' values will be included in the response in the same format as with the `Deals` endpoints. If a custom field's value hasn't been set for the lead, it won't appear in the response. Please note that leads do not have a separate set of custom fields, instead they inherit the custom fields' structure from deals.

API v1

###### Cost

20

###### Request

GET

/v1/leads

###### Query parameters

limit

integer

For pagination, the limit of entries to be returned. If not provided, 100 items will be returned.

start

integer

For pagination, the position that represents the first result for the page

owner\_id

integer

If supplied, only leads matching the given user will be returned. However, `filter_id` takes precedence over `owner_id` when supplied.

person\_id

integer

If supplied, only leads matching the given person will be returned. However, `filter_id` takes precedence over `person_id` when supplied.

organization\_id

integer

If supplied, only leads matching the given organization will be returned. However, `filter_id` takes precedence over `organization_id` when supplied.

filter\_id

integer

The ID of the filter to use

sort

string

The field names and sorting mode separated by a comma ( `field_name_1 ASC`, `field_name_2 DESC`). Only first-level field keys are supported (no nested keys).

Values

id

title

owner\_id

creator\_id

was\_seen

expected\_close\_date

next\_activity\_id

add\_time

update\_time

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":\[ ... \]

#### Get all archived leads

![Copy link](<Base64-Image-Removed>)

Returns multiple archived leads. Leads are sorted by the time they were created, from oldest to newest. Pagination can be controlled using `limit` and `start` query parameters. If a lead contains custom fields, the fields' values will be included in the response in the same format as with the `Deals` endpoints. If a custom field's value hasn't been set for the lead, it won't appear in the response. Please note that leads do not have a separate set of custom fields, instead they inherit the custom fields' structure from deals.

API v1

###### Cost

40

###### Request

GET

/v1/leads/archived

###### Query parameters

limit

integer

For pagination, the limit of entries to be returned. If not provided, 100 items will be returned.

start

integer

For pagination, the position that represents the first result for the page

owner\_id

integer

If supplied, only leads matching the given user will be returned. However, `filter_id` takes precedence over `owner_id` when supplied.

person\_id

integer

If supplied, only leads matching the given person will be returned. However, `filter_id` takes precedence over `person_id` when supplied.

organization\_id

integer

If supplied, only leads matching the given organization will be returned. However, `filter_id` takes precedence over `organization_id` when supplied.

filter\_id

integer

The ID of the filter to use

sort

string

The field names and sorting mode separated by a comma ( `field_name_1 ASC`, `field_name_2 DESC`). Only first-level field keys are supported (no nested keys).

Values

id

title

owner\_id

creator\_id

was\_seen

expected\_close\_date

next\_activity\_id

add\_time

update\_time

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":\[ ... \]

#### Get one lead

![Copy link](<Base64-Image-Removed>)

Returns details of a specific lead. If a lead contains custom fields, the fields' values will be included in the response in the same format as with the `Deals` endpoints. If a custom field's value hasn't been set for the lead, it won't appear in the response. Please note that leads do not have a separate set of custom fields, instead they inherit the custom fields’ structure from deals.

API v1

###### Cost

2

###### Request

GET

/v1/leads/{id}

###### Path parameters

id

string

required

The ID of the lead

Format

uuid

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }

#### List permitted users

![Copy link](<Base64-Image-Removed>)

Lists the users permitted to access a lead.

API v1

###### Cost

10

###### Request

GET

/v1/leads/{id}/permittedUsers

###### Path parameters

id

string

required

The ID of the lead

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":\[ ... \]

#### Search leads

![Copy link](<Base64-Image-Removed>)

Searches all leads by title, notes and/or custom fields. This endpoint is a wrapper of [/v1/itemSearch](https://developers.pipedrive.com/docs/api/v1/ItemSearch#searchItem) with a narrower OAuth scope. Found leads can be filtered by the person ID and the organization ID.

[View quick guide: /v1 to /v2 migration](https://pipedrive.readme.io/docs/pipedrive-api-v2-migration-guide)

API v1

API v2

###### Cost

20

###### Request

GET

/api/v2/leads/search

###### Query parameters

term

string

required

The search term to look for. Minimum 2 characters (or 1 if using `exact_match`). Please note that the search term has to be URL encoded.

fields

string

A comma-separated string array. The fields to perform the search from. Defaults to all of them.

Values

custom\_fields

notes

title

exact\_match

boolean

When enabled, only full exact matches against the given term are returned. It is **not** case sensitive.

person\_id

integer

Will filter leads by the provided person ID. The upper limit of found leads associated with the person is 2000.

organization\_id

integer

Will filter leads by the provided organization ID. The upper limit of found leads associated with the organization is 2000.

include\_fields

string

Supports including optional fields in the results which are not provided by default

Values

lead.was\_seen

limit

integer

For pagination, the limit of entries to be returned. If not provided, 100 items will be returned. Please note that a maximum value of 500 is allowed.

cursor

string

For pagination, the marker (an opaque string value) representing the first item on the next page

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }
- ▶


"additional\_data":{ ... }

#### Get Lead conversion status (BETA)

![Copy link](<Base64-Image-Removed>)

Returns data about the conversion. Status is always present and its value (not\_started, running, completed, failed, rejected) represents the current state of the conversion. Deal ID is only present if the conversion was successfully finished. This data is only temporary and removed after a few days.

API v2

Endpoint is in beta

###### Cost

1

###### Request

GET

/api/v2/leads/{id}/convert/status/{conversion\_id}

###### Path parameters

id

string

required

The ID of a lead

Format

uuid

conversion\_id

string

required

The ID of the conversion

Format

uuid

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }
- "additional\_data":null

#### Add a lead

![Copy link](<Base64-Image-Removed>)

Creates a lead. A lead always has to be linked to a person or an organization or both. All leads created through the Pipedrive API will have a lead source and origin set to `API`. Here's the tutorial for [adding a lead](https://pipedrive.readme.io/docs/adding-a-lead). If a lead contains custom fields, the fields' values will be included in the response in the same format as with the `Deals` endpoints. If a custom field's value hasn't been set for the lead, it won't appear in the response. Please note that leads do not have a separate set of custom fields, instead they inherit the custom fields' structure from deals. See an example given in the [updating custom fields' values tutorial](https://pipedrive.readme.io/docs/updating-custom-field-value).

API v1

###### Cost

10

###### Request

POST

/v1/leads

###### Body parameters

application/json

title

string

required

The name of the lead

owner\_id

integer

The ID of the user which will be the owner of the created lead. If not provided, the user making the request will be used.

label\_ids

array

The IDs of the lead labels which will be associated with the lead

person\_id

integer

The ID of a person which this lead will be linked to. If the person does not exist yet, it needs to be created first. This property is required unless `organization_id` is specified.

organization\_id

integer

The ID of an organization which this lead will be linked to. If the organization does not exist yet, it needs to be created first. This property is required unless `person_id` is specified.

value

object

The potential value of the lead represented by a JSON object: `{ "amount": 200, "currency": "EUR" }`. Both amount and currency are required.

expected\_close\_date

string

The date of when the deal which will be created from the lead is expected to be closed. In ISO 8601 format: YYYY-MM-DD.

Format

date

visible\_to

string

The visibility of the lead. If omitted, the visibility will be set to the default visibility setting of this item type for the authorized user. Read more about visibility groups [here](https://support.pipedrive.com/en/article/visibility-groups).

#### Essential / Advanced plan

| Value | Description |
| --- | --- |
| `1` | Owner & followers |
| `3` | Entire company |

#### Professional / Enterprise plan

| Value | Description |
| --- | --- |
| `1` | Owner only |
| `3` | Owner's visibility group |
| `5` | Owner's visibility group and sub-groups |
| `7` | Entire company |

Values

1

3

5

7

was\_seen

boolean

A flag indicating whether the lead was seen by someone in the Pipedrive UI

origin\_id

string

The optional ID to further distinguish the origin of the lead - e.g. Which API integration created this lead. If omitted, `origin_id` will be set to null.

channel

integer

The ID of Marketing channel this lead was created from. Provided value must be one of the channels configured for your company. You can fetch allowed values with [GET /v1/dealFields](https://developers.pipedrive.com/docs/api/v1/DealFields#getDealField). If omitted, channel will be set to null.

channel\_id

string

The optional ID to further distinguish the Marketing channel. If omitted, `channel_id` will be set to null.

###### Response

201

Created

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }

#### Convert a lead to a deal (BETA)

![Copy link](<Base64-Image-Removed>)

Initiates a conversion of a lead to a deal. The return value is an ID of a job that was assigned to perform the conversion. Related entities (notes, files, emails, activities, ...) are transferred during the process to the target entity. If the conversion is successful, the lead is marked as deleted. To retrieve the created entity ID and the result of the conversion, call the [/api/v2/leads/{lead\_id}/convert/status/{conversion\_id}](https://developers.pipedrive.com/docs/api/v1/Leads#getLeadConversionStatus) endpoint.

API v2

Endpoint is in beta

###### Cost

40

###### Request

POST

/api/v2/leads/{id}/convert/deal

###### Path parameters

id

string

required

The ID of the lead to convert

Format

uuid

###### Body parameters

application/json

stage\_id

integer

The ID of a stage the created deal will be added to. Please note that a pipeline will be assigned automatically based on the `stage_id`. If omitted, the deal will be placed in the first stage of the default pipeline.

pipeline\_id

integer

The ID of a pipeline the created deal will be added to. By default, the deal will be added to the first stage of the specified pipeline. Please note that `pipeline_id` and `stage_id` should not be used together as `pipeline_id` will be ignored.

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }
- "additional\_data":null

#### Update a lead

![Copy link](<Base64-Image-Removed>)

Updates one or more properties of a lead. Only properties included in the request will be updated. Send `null` to unset a property (applicable for example for `value`, `person_id` or `organization_id`). If a lead contains custom fields, the fields' values will be included in the response in the same format as with the `Deals` endpoints. If a custom field's value hasn't been set for the lead, it won't appear in the response. Please note that leads do not have a separate set of custom fields, instead they inherit the custom fields’ structure from deals. See an example given in the [updating custom fields’ values tutorial](https://pipedrive.readme.io/docs/updating-custom-field-value).

API v1

###### Cost

10

###### Request

PATCH

/v1/leads/{id}

###### Path parameters

id

string

required

The ID of the lead

Format

uuid

###### Body parameters

application/json

title

string

The name of the lead

owner\_id

integer

The ID of the user which will be the owner of the created lead. If not provided, the user making the request will be used.

label\_ids

array

The IDs of the lead labels which will be associated with the lead

person\_id

integer

The ID of a person which this lead will be linked to. If the person does not exist yet, it needs to be created first. A lead always has to be linked to a person or organization or both.

organization\_id

integer

The ID of an organization which this lead will be linked to. If the organization does not exist yet, it needs to be created first. A lead always has to be linked to a person or organization or both.

is\_archived

boolean

A flag indicating whether the lead is archived or not

value

object

The potential value of the lead represented by a JSON object: `{ "amount": 200, "currency": "EUR" }`. Both amount and currency are required.

expected\_close\_date

string

The date of when the deal which will be created from the lead is expected to be closed. In ISO 8601 format: YYYY-MM-DD.

Format

date

visible\_to

string

The visibility of the lead. If omitted, the visibility will be set to the default visibility setting of this item type for the authorized user. Read more about visibility groups [here](https://support.pipedrive.com/en/article/visibility-groups).

#### Essential / Advanced plan

| Value | Description |
| --- | --- |
| `1` | Owner & followers |
| `3` | Entire company |

#### Professional / Enterprise plan

| Value | Description |
| --- | --- |
| `1` | Owner only |
| `3` | Owner's visibility group |
| `5` | Owner's visibility group and sub-groups |
| `7` | Entire company |

Values

1

3

5

7

was\_seen

boolean

A flag indicating whether the lead was seen by someone in the Pipedrive UI

channel

integer

The ID of Marketing channel this lead was created from. Provided value must be one of the channels configured for your company which you can fetch with [GET /v1/dealFields](https://developers.pipedrive.com/docs/api/v1/DealFields#getDealField).

channel\_id

string

The optional ID to further distinguish the Marketing channel.

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }

#### Delete a lead

![Copy link](<Base64-Image-Removed>)

Deletes a specific lead.

API v1

###### Cost

6

###### Request

DELETE

/v1/leads/{id}

###### Path parameters

id

string

required

The ID of the lead

Format

uuid

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }

### Subscribe to Pipedrive’s Developer Newsletter

Your email address

Subscribe

We promise not to send you any marketing materials or spam, just developer news.

Copy to clipboard

Copy to clipboard

Copy to clipboard

Copy to clipboard

Copy to clipboard

Copy to clipboard

Copy to clipboard

Copy to clipboard

Copy to clipboard

Copy to clipboard

By clicking “Accept All”, you agree to the storing of cookies on your device to enhance site navigation, analyze site usage, personalize content and serve personalized advertisements. [Cookie Notice](https://www.pipedrive.com/en/cookie-notice) [Privacy Notice](https://www.pipedrive.com/en/privacy)

Cookies Settings

Reject AllAccept All

![Company Logo](https://cdn.cookielaw.org/logos/93bc8daa-5b3a-4f92-bef0-2fbea0b508b4/a8118b39-c260-48e7-b195-9437d7861070/1535dff4-8ba4-42fc-9b10-12667500f44c/Pipedrive_Logo_Green.png)

## Privacy Preference Center

When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer.


[More information](https://www.pipedrive.com/en/privacy)

Allow All

### Manage Consent Preferences

#### Performance Cookies

Performance Cookies

These cookies allow us to count visits and traffic sources so we can measure and improve the performance of our site. They help us to know which pages are the most and least popular and see how visitors move around the site.    All information these cookies collect is aggregated and therefore anonymous. If you do not allow these cookies we will not know when you have visited our site, and will not be able to monitor its performance.

#### Targeting Cookies

Targeting Cookies

These cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant adverts on other sites.    They do not store directly personal information, but are based on uniquely identifying your browser and internet device. If you do not allow these cookies, you will experience less targeted advertising.

#### Functional Cookies

Functional Cookies

These cookies enable the website to provide enhanced functionality and personalisation. They may be set by us or by third party providers whose services we have added to our pages.    If you do not allow these cookies then some or all of these services may not function properly.

#### Strictly Necessary Cookies

Always Active

These cookies are necessary for the website to function and cannot be switched off in our systems. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, logging in or filling in forms. You can set your browser to block or alert you about these cookies, but some parts of the site will not then work. These cookies do not store any personally identifiable information.

Back Button

### Cookie List

Search Icon

Filter Icon

Clear

checkbox labellabel

ApplyCancel

ConsentLeg.Interest

checkbox labellabel

checkbox labellabel

checkbox labellabel

Reject AllConfirm My Choices

[![Powered by Onetrust](https://cdn.cookielaw.org/logos/static/powered_by_logo.svg)](https://www.onetrust.com/products/cookie-consent/)