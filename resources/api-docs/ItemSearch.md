---
url: "https://developers.pipedrive.com/docs/api/v1/ItemSearch"
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

[GET\\
\\
Perform a search from multiple item types](https://developers.pipedrive.com/docs/api/v1/ItemSearch#searchItem)

[GET\\
\\
Perform a search using a specific field from an item type](https://developers.pipedrive.com/docs/api/v1/ItemSearch#searchItemByField)

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

## ItemSearch

Run in Postman

Ordered reference objects, pointing to either deals, persons, organizations, leads, products, files or mail attachments.

#### Perform a search from multiple item types

![Copy link](<Base64-Image-Removed>)

Performs a search from your choice of item types and fields.

[View quick guide: /v1 to /v2 migration](https://pipedrive.readme.io/docs/pipedrive-api-v2-migration-guide)

API v1

API v2

###### Cost

20

###### Request

GET

/api/v2/itemSearch

###### Query parameters

term

string

required

The search term to look for. Minimum 2 characters (or 1 if using `exact_match`). Please note that the search term has to be URL encoded.

item\_types

string

A comma-separated string array. The type of items to perform the search from. Defaults to all.

Values

deal

person

organization

product

lead

file

mail\_attachment

project

fields

string

A comma-separated string array. The fields to perform the search from. Defaults to all. Relevant for each item type are:

| **Item type** | **Field** |
| --- | --- |
| Deal | `custom_fields`, `notes`, `title` |
| Person | `custom_fields`, `email`, `name`, `notes`, `phone` |
| Organization | `address`, `custom_fields`, `name`, `notes` |
| Product | `code`, `custom_fields`, `name` |
| Lead | `custom_fields`, `notes`, `email`, `organization_name`, `person_name`, `phone`, `title` |
| File | `name` |
| Mail attachment | `name` |
| Project | `custom_fields`, `notes`, `title`, `description` |

Only the following custom field types are searchable: `address`, `varchar`, `text`, `varchar_auto`, `double`, `monetary` and `phone`. Read more about searching by custom fields [here](https://support.pipedrive.com/en/article/search-finding-what-you-need#searching-by-custom-fields).

When searching for leads, the email, organization\_name, person\_name, and phone fields will return results only for leads not linked to contacts. For searching leads by person or organization values, please use `search_for_related_items`.

Values

address

code

custom\_fields

email

name

notes

organization\_name

person\_name

phone

title

description

search\_for\_related\_items

boolean

When enabled, the response will include up to 100 newest related leads and 100 newest related deals for each found person and organization and up to 100 newest related persons for each found organization

exact\_match

boolean

When enabled, only full exact matches against the given term are returned. It is **not** case sensitive.

include\_fields

string

A comma-separated string array. Supports including optional fields in the results which are not provided by default.

Values

deal.cc\_email

person.picture

product.price

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

#### Perform a search using a specific field from an item type

![Copy link](<Base64-Image-Removed>)

Performs a search from the values of a specific field. Results can either be the distinct values of the field (useful for searching autocomplete field values), or the IDs of actual items (deals, leads, persons, organizations or products).

[View quick guide: /v1 to /v2 migration](https://pipedrive.readme.io/docs/pipedrive-api-v2-migration-guide)

API v1

API v2

###### Cost

20

###### Request

GET

/api/v2/itemSearch/field

###### Query parameters

term

string

required

The search term to look for. Minimum 2 characters (or 1 if `match` is `exact`). Please note that the search term has to be URL encoded.

entity\_type

string

required

The type of the field to perform the search from

Values

deal

lead

person

organization

product

project

match

string

The type of match used against the term. The search **is** case sensitive.

E.g. in case of searching for a value `monkey`,

- with `exact` match, you will only find it if term is `monkey`
- with `beginning` match, you will only find it if the term matches the beginning or the whole string, e.g. `monk` and `monkey`
- with `middle` match, you will find the it if the term matches any substring of the value, e.g. `onk` and `ke`

.

Default

exact

Values

exact

beginning

middle

field

string

required

The key of the field to search from. The field key can be obtained by fetching the list of the fields using any of the fields' API GET methods (dealFields, personFields, etc.). Only the following custom field types are searchable: `address`, `varchar`, `text`, `varchar_auto`, `double`, `monetary` and `phone`. Read more about searching by custom fields [here](https://support.pipedrive.com/en/article/search-finding-what-you-need#searching-by-custom-fields).

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

### Subscribe to Pipedrive’s Developer Newsletter

Your email address

Subscribe

We promise not to send you any marketing materials or spam, just developer news.

Copy to clipboard

Copy to clipboard