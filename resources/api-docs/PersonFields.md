---
url: "https://developers.pipedrive.com/docs/api/v1/PersonFields"
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

[OrganizationFields](https://developers.pipedrive.com/docs/api/v1/OrganizationFields)

[OrganizationRelationships](https://developers.pipedrive.com/docs/api/v1/OrganizationRelationships)

[PermissionSets](https://developers.pipedrive.com/docs/api/v1/PermissionSets)

[Persons](https://developers.pipedrive.com/docs/api/v1/Persons)

[PersonFields](https://developers.pipedrive.com/docs/api/v1/PersonFields)

[GET\\
\\
Get all person fields](https://developers.pipedrive.com/docs/api/v1/PersonFields#getPersonFields)

[GET\\
\\
Get one person field](https://developers.pipedrive.com/docs/api/v1/PersonFields#getPersonField)

[POST\\
\\
Add a new person field](https://developers.pipedrive.com/docs/api/v1/PersonFields#addPersonField)

[PUT\\
\\
Update a person field](https://developers.pipedrive.com/docs/api/v1/PersonFields#updatePersonField)

[DELETE\\
\\
Delete multiple person fields in bulk](https://developers.pipedrive.com/docs/api/v1/PersonFields#deletePersonFields)

[DELETE\\
\\
Delete a person field](https://developers.pipedrive.com/docs/api/v1/PersonFields#deletePersonField)

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

## PersonFields

Run in Postman

Person fields represent the near-complete schema for a person in the context of the company of the authorized user. Each company can have a different schema for their persons, with various custom fields. In the context of using person fields as a schema for defining the data fields of a person, it must be kept in mind that some types of custom fields can have additional data fields which are not separate person fields per se. Such is the case with monetary, daterange and timerange fields – each of these fields will have one additional data field in addition to the one presented in the context of person fields. For example, if there is a monetary field with the key `ffk9s9` stored on the account, `ffk9s9` would hold the numeric value of the field, and `ffk9s9_currency` would hold the ISO currency code that goes along with the numeric value. To find out which data fields are available, fetch one person and list its keys.

#### Get all person fields

![Copy link](<Base64-Image-Removed>)

Returns data about all person fields.

If a company uses the [Campaigns product](https://pipedrive.readme.io/docs/campaigns-in-pipedrive-api), then this endpoint will also return the `data.marketing_status` field.

API v1

###### Cost

20

###### Request

GET

/v1/personFields

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

#### Get one person field

![Copy link](<Base64-Image-Removed>)

Returns data about a specific person field.

API v1

###### Cost

2

###### Request

GET

/v1/personFields/{id}

###### Path parameters

id

integer

required

The ID of the field

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }

#### Add a new person field

![Copy link](<Base64-Image-Removed>)

Adds a new person field. For more information, see the tutorial for [adding a new custom field](https://pipedrive.readme.io/docs/adding-a-new-custom-field).

API v1

###### Cost

10

###### Request

POST

/v1/personFields

###### Body parameters

application/json

name

string

required

The name of the field

options

array

When `field_type` is either set or enum, possible options must be supplied as a JSON-encoded sequential array of objects. Example: `[{"label":"New Item"}]`

add\_visible\_flag

boolean

Whether the field is available in the 'add new' modal or not (both in the web and mobile app)

Default

true

field\_type

string

required

The type of the field

| Value | Description |
| --- | --- |
| `address` | Address field |
| `date` | Date (format YYYY-MM-DD) |
| `daterange` | Date-range field (has a start date and end date value, both YYYY-MM-DD) |
| `double` | Numeric value |
| `enum` | Options field with a single possible chosen option |

| `monetary` | Monetary field (has a numeric value and a currency value) |
| `org` | Organization field (contains an organization ID which is stored on the same account) |
| `people` | Person field (contains a person ID which is stored on the same account) |
| `phone` | Phone field (up to 255 numbers and/or characters) |
| `set` | Options field with a possibility of having multiple chosen options |
| `text` | Long text (up to 65k characters) |
| `time` | Time field (format HH:MM:SS) |
| `timerange` | Time-range field (has a start time and end time value, both HH:MM:SS) |
| `user` | User field (contains a user ID of another Pipedrive user) |
| `varchar` | Text (up to 255 characters) |
| `varchar_auto` | Autocomplete text (up to 255 characters) |
| `visible_to` | System field that keeps item's visibility setting |

Values

address

date

daterange

double

enum

monetary

org

people

phone

set

text

time

timerange

user

varchar

varchar\_auto

visible\_to

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }

#### Update a person field

![Copy link](<Base64-Image-Removed>)

Updates a person field. For more information, see the tutorial for [updating custom fields' values](https://pipedrive.readme.io/docs/updating-custom-field-value).

API v1

###### Cost

10

###### Request

PUT

/v1/personFields/{id}

###### Path parameters

id

integer

required

The ID of the field

###### Body parameters

application/json

name

string

The name of the field

options

array

When `field_type` is either set or enum, possible options must be supplied as a JSON-encoded sequential array of objects. All active items must be supplied and already existing items must have their ID supplied. New items only require a label. Example: `[{"id":123,"label":"Existing Item"},{"label":"New Item"}]`

add\_visible\_flag

boolean

Whether the field is available in 'add new' modal or not (both in web and mobile app)

Default

true

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }

#### Delete multiple person fields in bulk

![Copy link](<Base64-Image-Removed>)

Marks multiple fields as deleted.

API v1

###### Cost

10

###### Request

DELETE

/v1/personFields

###### Query parameters

ids

string

required

The comma-separated field IDs to delete

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }

#### Delete a person field

![Copy link](<Base64-Image-Removed>)

Marks a field as deleted. For more information, see the tutorial for [deleting a custom field](https://pipedrive.readme.io/docs/deleting-a-custom-field).

API v1

###### Cost

6

###### Request

DELETE

/v1/personFields/{id}

###### Path parameters

id

integer

required

The ID of the field

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