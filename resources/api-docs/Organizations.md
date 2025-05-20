---
url: "https://developers.pipedrive.com/docs/api/v1/Organizations"
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

[LeadLabels](https://developers.pipedrive.com/docs/api/v1/LeadLabels)

[LeadSources](https://developers.pipedrive.com/docs/api/v1/LeadSources)

[LegacyTeams](https://developers.pipedrive.com/docs/api/v1/LegacyTeams)

[Mailbox](https://developers.pipedrive.com/docs/api/v1/Mailbox)

[Meetings](https://developers.pipedrive.com/docs/api/v1/Meetings)

[Notes](https://developers.pipedrive.com/docs/api/v1/Notes)

[NoteFields](https://developers.pipedrive.com/docs/api/v1/NoteFields)

[OAuth 2.0](https://developers.pipedrive.com/docs/api/v1/Oauth)

[Organizations](https://developers.pipedrive.com/docs/api/v1/Organizations)

[GET\\
\\
Get all organizations](https://developers.pipedrive.com/docs/api/v1/Organizations#getOrganizations)

[GET\\
\\
Get all organizations collection](https://developers.pipedrive.com/docs/api/v1/Organizations#getOrganizationsCollection)

[GET\\
\\
Search organizations](https://developers.pipedrive.com/docs/api/v1/Organizations#searchOrganization)

[GET\\
\\
Get details of an organization](https://developers.pipedrive.com/docs/api/v1/Organizations#getOrganization)

[GET\\
\\
List activities associated with an organization](https://developers.pipedrive.com/docs/api/v1/Organizations#getOrganizationActivities)

[GET\\
\\
List updates about organization field values](https://developers.pipedrive.com/docs/api/v1/Organizations#getOrganizationChangelog)

[GET\\
\\
List deals associated with an organization](https://developers.pipedrive.com/docs/api/v1/Organizations#getOrganizationDeals)

[GET\\
\\
List files attached to an organization](https://developers.pipedrive.com/docs/api/v1/Organizations#getOrganizationFiles)

[GET\\
\\
List updates about an organization](https://developers.pipedrive.com/docs/api/v1/Organizations#getOrganizationUpdates)

[GET\\
\\
List followers of an organization](https://developers.pipedrive.com/docs/api/v1/Organizations#getOrganizationFollowers)

[GET\\
\\
List mail messages associated with an organization](https://developers.pipedrive.com/docs/api/v1/Organizations#getOrganizationMailMessages)

[GET\\
\\
List permitted users](https://developers.pipedrive.com/docs/api/v1/Organizations#getOrganizationUsers)

[GET\\
\\
List persons of an organization](https://developers.pipedrive.com/docs/api/v1/Organizations#getOrganizationPersons)

[GET\\
\\
List followers changelog of an organization](https://developers.pipedrive.com/docs/api/v1/Organizations#getOrganizationFollowersChangelog)

[POST\\
\\
Add an organization](https://developers.pipedrive.com/docs/api/v1/Organizations#addOrganization)

[POST\\
\\
Add a follower to an organization](https://developers.pipedrive.com/docs/api/v1/Organizations#addOrganizationFollower)

[PATCH\\
\\
Update an organization](https://developers.pipedrive.com/docs/api/v1/Organizations#updateOrganization)

[PUT\\
\\
Merge two organizations](https://developers.pipedrive.com/docs/api/v1/Organizations#mergeOrganizations)

[DELETE\\
\\
Delete multiple organizations in bulk](https://developers.pipedrive.com/docs/api/v1/Organizations#deleteOrganizations)

[DELETE\\
\\
Delete an organization](https://developers.pipedrive.com/docs/api/v1/Organizations#deleteOrganization)

[DELETE\\
\\
Delete a follower from an organization](https://developers.pipedrive.com/docs/api/v1/Organizations#deleteOrganizationFollower)

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

## Organizations

Run in Postman

Organizations are companies and other kinds of organizations you are making deals with. Persons can be associated with organizations so that each organization can contain one or more persons.

#### Get all organizations

![Copy link](<Base64-Image-Removed>)

Returns data about all organizations.

[View quick guide: /v1 to /v2 migration](https://pipedrive.readme.io/docs/pipedrive-api-v2-migration-guide)

API v1

API v2

###### Cost

10

###### Request

GET

/api/v2/organizations

###### Query parameters

filter\_id

integer

If supplied, only organizations matching the specified filter are returned

ids

string

Optional comma separated string array of up to 100 entity ids to fetch. If filter\_id is provided, this is ignored. If any of the requested entities do not exist or are not visible, they are not included in the response.

owner\_id

integer

If supplied, only organization owned by the specified user are returned. If filter\_id is provided, this is ignored.

updated\_since

string

If set, only organizations with an `update_time` later than or equal to this time are returned. In RFC3339 format, e.g. 2025-01-01T10:20:00Z.

updated\_until

string

If set, only organizations with an `update_time` earlier than this time are returned. In RFC3339 format, e.g. 2025-01-01T10:20:00Z.

sort\_by

string

The field to sort by. Supported fields: `id`, `update_time`, `add_time`.

Default

id

Values

id

update\_time

add\_time

sort\_direction

string

The sorting direction. Supported values: `asc`, `desc`.

Default

asc

Values

asc

desc

include\_fields

string

Optional comma separated string array of additional fields to include

Values

next\_activity\_id

last\_activity\_id

open\_deals\_count

related\_open\_deals\_count

closed\_deals\_count

related\_closed\_deals\_count

email\_messages\_count

people\_count

activities\_count

done\_activities\_count

undone\_activities\_count

files\_count

notes\_count

followers\_count

won\_deals\_count

related\_won\_deals\_count

lost\_deals\_count

related\_lost\_deals\_count

custom\_fields

string

Optional comma separated string array of custom fields keys to include. If you are only interested in a particular set of custom fields, please use this parameter for faster results and smaller response.

A maximum of 15 keys is allowed.

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


"data":\[ ... \]
- ▶


"additional\_data":{ ... }

#### Get all organizations collection

![Copy link](<Base64-Image-Removed>)

Returns all organizations. Please note that only global admins (those with global permissions) can access this endpoint. Users with regular permissions will receive a 403 response. Read more about global permissions [here](https://support.pipedrive.com/en/article/global-user-management).

This endpoint has been deprecated. Please use [GET /api/v2/organizations](https://developers.pipedrive.com/docs/api/v1/Organizations#getOrganizations) instead.

Deprecated endpoint

###### Cost

10

###### Request

GET

/v1/organizations/collection

###### Query parameters

cursor

string

For pagination, the marker (an opaque string value) representing the first item on the next page

limit

integer

For pagination, the limit of entries to be returned. If not provided, 100 items will be returned. Please note that a maximum value of 500 is allowed.

since

string

The time boundary that points to the start of the range of data. Datetime in ISO 8601 format. E.g. 2022-11-01 08:55:59. Operates on the `update_time` field.

until

string

The time boundary that points to the end of the range of data. Datetime in ISO 8601 format. E.g. 2022-11-01 08:55:59. Operates on the `update_time` field.

owner\_id

integer

If supplied, only organizations owned by the given user will be returned

first\_char

string

If supplied, only organizations whose name starts with the specified letter will be returned (case-insensitive)

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":\[ ... \]
- ▶


"additional\_data":{ ... }

#### Search organizations

![Copy link](<Base64-Image-Removed>)

Searches all organizations by name, address, notes and/or custom fields. This endpoint is a wrapper of [/v1/itemSearch](https://developers.pipedrive.com/docs/api/v1/ItemSearch#searchItem) with a narrower OAuth scope.

[View quick guide: /v1 to /v2 migration](https://pipedrive.readme.io/docs/pipedrive-api-v2-migration-guide)

API v1

API v2

###### Cost

20

###### Request

GET

/api/v2/organizations/search

###### Query parameters

term

string

required

The search term to look for. Minimum 2 characters (or 1 if using `exact_match`). Please note that the search term has to be URL encoded.

fields

string

A comma-separated string array. The fields to perform the search from. Defaults to all of them. Only the following custom field types are searchable: `address`, `varchar`, `text`, `varchar_auto`, `double`, `monetary` and `phone`. Read more about searching by custom fields [here](https://support.pipedrive.com/en/article/search-finding-what-you-need#searching-by-custom-fields).

Values

address

custom\_fields

notes

name

exact\_match

boolean

When enabled, only full exact matches against the given term are returned. It is **not** case sensitive.

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

#### Get details of an organization

![Copy link](<Base64-Image-Removed>)

Returns the details of a specific organization.

[View quick guide: /v1 to /v2 migration](https://pipedrive.readme.io/docs/pipedrive-api-v2-migration-guide)

API v1

API v2

###### Cost

1

###### Request

GET

/api/v2/organizations/{id}

###### Path parameters

id

integer

required

The ID of the organization

###### Query parameters

include\_fields

string

Optional comma separated string array of additional fields to include

Values

next\_activity\_id

last\_activity\_id

open\_deals\_count

related\_open\_deals\_count

closed\_deals\_count

related\_closed\_deals\_count

email\_messages\_count

people\_count

activities\_count

done\_activities\_count

undone\_activities\_count

files\_count

notes\_count

followers\_count

won\_deals\_count

related\_won\_deals\_count

lost\_deals\_count

related\_lost\_deals\_count

custom\_fields

string

Optional comma separated string array of custom fields keys to include. If you are only interested in a particular set of custom fields, please use this parameter for faster results and smaller response.

A maximum of 15 keys is allowed.

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }

#### List activities associated with an organization

![Copy link](<Base64-Image-Removed>)

Lists activities associated with an organization.

This endpoint has been deprecated. Please use [GET /api/v2/activities?org\_id={id}](https://developers.pipedrive.com/docs/api/v1/Activities#getActivities) instead.

Deprecated endpoint

###### Cost

20

###### Request

GET

/v1/organizations/{id}/activities

###### Path parameters

id

integer

required

The ID of the organization

###### Query parameters

start

integer

Pagination start

Default

0

limit

integer

Items shown per page

done

number

Whether the activity is done or not. 0 = Not done, 1 = Done. If omitted returns both Done and Not done activities.

Values

0

1

exclude

string

A comma-separated string of activity IDs to exclude from result

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":\[ ... \]
- ▶


"additional\_data":{ ... }

#### List updates about organization field values

![Copy link](<Base64-Image-Removed>)

Lists updates about field values of an organization.

API v1

###### Cost

20

###### Request

GET

/v1/organizations/{id}/changelog

###### Path parameters

id

integer

required

The ID of the organization

###### Query parameters

cursor

string

For pagination, the marker (an opaque string value) representing the first item on the next page

limit

integer

Items shown per page

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":\[ ... \]
- ▶


"additional\_data":{ ... }

#### List deals associated with an organization

![Copy link](<Base64-Image-Removed>)

Lists deals associated with an organization.

This endpoint has been deprecated. Please use [GET /api/v2/deals?org\_id={id}](https://developers.pipedrive.com/docs/api/v1/Deals#getDeals) instead.

Deprecated endpoint

###### Cost

20

###### Request

GET

/v1/organizations/{id}/deals

###### Path parameters

id

integer

required

The ID of the organization

###### Query parameters

start

integer

Pagination start

Default

0

limit

integer

Items shown per page

status

string

Only fetch deals with a specific status. If omitted, all not deleted deals are returned. If set to deleted, deals that have been deleted up to 30 days ago will be included.

Default

all\_not\_deleted

Values

open

won

lost

deleted

all\_not\_deleted

sort

string

The field names and sorting mode separated by a comma ( `field_name_1 ASC`, `field_name_2 DESC`). Only first-level field keys are supported (no nested keys).

only\_primary\_association

number

If set, only deals that are directly associated to the organization are fetched. If not set (default), all deals are fetched that are either directly or indirectly related to the organization. Indirect relations include relations through custom, organization-type fields and through persons of the given organization.

Values

0

1

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":\[ ... \]
- ▶


"additional\_data":{ ... }
- ▶


"related\_objects":{ ... }

#### List files attached to an organization

![Copy link](<Base64-Image-Removed>)

Lists files associated with an organization.

API v1

###### Cost

20

###### Request

GET

/v1/organizations/{id}/files

###### Path parameters

id

integer

required

The ID of the organization

###### Query parameters

start

integer

Pagination start

Default

0

limit

integer

Items shown per page. Please note that a maximum value of 100 is allowed.

sort

string

Supported fields: `id`, `update_time`

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":\[ ... \]
- ▶


"additional\_data":{ ... }

#### List updates about an organization

![Copy link](<Base64-Image-Removed>)

Lists updates about an organization.

API v1

###### Cost

40

###### Request

GET

/v1/organizations/{id}/flow

###### Path parameters

id

integer

required

The ID of the organization

###### Query parameters

start

integer

Pagination start

Default

0

limit

integer

Items shown per page

all\_changes

string

Whether to show custom field updates or not. 1 = Include custom field changes. If omitted, returns changes without custom field updates.

items

string

A comma-separated string for filtering out item specific updates. (Possible values - activity, plannedActivity, note, file, change, deal, follower, participant, mailMessage, mailMessageWithAttachment, invoice, activityFile, document).

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":\[ ... \]
- ▶


"additional\_data":{ ... }
- ▶


"related\_objects":{ ... }

#### List followers of an organization

![Copy link](<Base64-Image-Removed>)

Lists users who are following the organization.

[View quick guide: /v1 to /v2 migration](https://pipedrive.readme.io/docs/pipedrive-api-v2-migration-guide)

API v1

API v2

###### Cost

10

###### Request

GET

/api/v2/organizations/{id}/followers

###### Path parameters

id

integer

required

The ID of the organization

###### Query parameters

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


"data":\[ ... \]
- ▶


"additional\_data":{ ... }

#### List mail messages associated with an organization

![Copy link](<Base64-Image-Removed>)

Lists mail messages associated with an organization.

API v1

###### Cost

20

###### Request

GET

/v1/organizations/{id}/mailMessages

###### Path parameters

id

integer

required

The ID of the organization

###### Query parameters

start

integer

Pagination start

Default

0

limit

integer

Items shown per page

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":\[ ... \]
- ▶


"additional\_data":{ ... }

#### List permitted users

![Copy link](<Base64-Image-Removed>)

List users permitted to access an organization.

API v1

###### Cost

10

###### Request

GET

/v1/organizations/{id}/permittedUsers

###### Path parameters

id

integer

required

The ID of the organization

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":\[ ... \]

#### List persons of an organization

![Copy link](<Base64-Image-Removed>)

Lists persons associated with an organization.

If a company uses the [Campaigns product](https://pipedrive.readme.io/docs/campaigns-in-pipedrive-api), then this endpoint will also return the `data.marketing_status` field.

This endpoint has been deprecated. Please use [GET /api/v2/persons?org\_id={id}](https://developers.pipedrive.com/docs/api/v1/Persons#getPersons) instead.

Deprecated endpoint

###### Cost

20

###### Request

GET

/v1/organizations/{id}/persons

###### Path parameters

id

integer

required

The ID of the organization

###### Query parameters

start

integer

Pagination start

Default

0

limit

integer

Items shown per page

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":\[ ... \]
- ▶


"additional\_data":{ ... }
- ▶


"related\_objects":{ ... }

#### List followers changelog of an organization

![Copy link](<Base64-Image-Removed>)

Lists changelogs about users have followed the organization.

API v2

###### Cost

10

###### Request

GET

/api/v2/organizations/{id}/followers/changelog

###### Path parameters

id

integer

required

The ID of the organization

###### Query parameters

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


"data":\[ ... \]
- ▶


"additional\_data":{ ... }

#### Add an organization

![Copy link](<Base64-Image-Removed>)

Adds a new organization.

[View quick guide: /v1 to /v2 migration](https://pipedrive.readme.io/docs/pipedrive-api-v2-migration-guide)

API v1

API v2

###### Cost

5

###### Request

POST

/api/v2/organizations

###### Body parameters

application/json

name

string

The name of the organization

owner\_id

integer

The ID of the user who owns the organization

add\_time

string

The creation date and time of the organization

update\_time

string

The last updated date and time of the organization

visible\_to

integer

The visibility of the organization

label\_ids

array

The IDs of labels assigned to the organization

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }

#### Add a follower to an organization

![Copy link](<Base64-Image-Removed>)

Adds a user as a follower to the organization.

[View quick guide: /v1 to /v2 migration](https://pipedrive.readme.io/docs/pipedrive-api-v2-migration-guide)

API v1

API v2

###### Cost

5

###### Request

POST

/api/v2/organizations/{id}/followers

###### Path parameters

id

integer

required

The ID of the organization

###### Body parameters

application/json

user\_id

integer

required

The ID of the user to add as a follower

###### Response

201

Created

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }

#### Update an organization

![Copy link](<Base64-Image-Removed>)

Updates the properties of a organization.

[View quick guide: /v1 to /v2 migration](https://pipedrive.readme.io/docs/pipedrive-api-v2-migration-guide)

API v1

API v2

###### Cost

5

###### Request

PATCH

/api/v2/organizations/{id}

###### Path parameters

id

integer

required

The ID of the organization

###### Body parameters

application/json

name

string

The name of the organization

owner\_id

integer

The ID of the user who owns the organization

add\_time

string

The creation date and time of the organization

update\_time

string

The last updated date and time of the organization

visible\_to

integer

The visibility of the organization

label\_ids

array

The IDs of labels assigned to the organization

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }

#### Merge two organizations

![Copy link](<Base64-Image-Removed>)

Merges an organization with another organization. For more information, see the tutorial for [merging two organizations](https://pipedrive.readme.io/docs/merging-two-organizations).

API v1

###### Cost

40

###### Request

PUT

/v1/organizations/{id}/merge

###### Path parameters

id

integer

required

The ID of the organization

###### Body parameters

application/json

merge\_with\_id

integer

required

The ID of the organization that the organization will be merged with

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }

#### Delete multiple organizations in bulk

![Copy link](<Base64-Image-Removed>)

Marks multiple organizations as deleted. After 30 days, the organizations will be permanently deleted.

This endpoint has been deprecated. Please use [DELETE /api/v2/organizations/{id}](https://developers.pipedrive.com/docs/api/v1/Organizations#deleteOrganization) instead.

Deprecated endpoint

###### Cost

10

###### Request

DELETE

/v1/organizations

###### Query parameters

ids

string

required

The comma-separated IDs that will be deleted

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }

#### Delete an organization

![Copy link](<Base64-Image-Removed>)

Marks a organization as deleted. After 30 days, the organization will be permanently deleted.

[View quick guide: /v1 to /v2 migration](https://pipedrive.readme.io/docs/pipedrive-api-v2-migration-guide)

API v1

API v2

###### Cost

3

###### Request

DELETE

/api/v2/organizations/{id}

###### Path parameters

id

integer

required

The ID of the organization

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }

#### Delete a follower from an organization

![Copy link](<Base64-Image-Removed>)

Deletes a user follower from the organization.

[View quick guide: /v1 to /v2 migration](https://pipedrive.readme.io/docs/pipedrive-api-v2-migration-guide)

API v1

API v2

###### Cost

3

###### Request

DELETE

/api/v2/organizations/{id}/followers/{follower\_id}

###### Path parameters

id

integer

required

The ID of the organization

follower\_id

integer

required

The ID of the following user

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