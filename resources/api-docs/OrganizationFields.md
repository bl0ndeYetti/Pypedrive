---
url: "https://developers.pipedrive.com/docs/api/v1/OrganizationFields"
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

[GET\\
\\
Get all organization fields](https://developers.pipedrive.com/docs/api/v1/OrganizationFields#getOrganizationFields)

[GET\\
\\
Get one organization field](https://developers.pipedrive.com/docs/api/v1/OrganizationFields#getOrganizationField)

[POST\\
\\
Add a new organization field](https://developers.pipedrive.com/docs/api/v1/OrganizationFields#addOrganizationField)

[PUT\\
\\
Update an organization field](https://developers.pipedrive.com/docs/api/v1/OrganizationFields#updateOrganizationField)

[DELETE\\
\\
Delete multiple organization fields in bulk](https://developers.pipedrive.com/docs/api/v1/OrganizationFields#deleteOrganizationFields)

[DELETE\\
\\
Delete an organization field](https://developers.pipedrive.com/docs/api/v1/OrganizationFields#deleteOrganizationField)

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

## OrganizationFields

Run in Postman

Organization fields represent the near-complete schema for an organization in the context of the company of the authorized user. Each company can have a different schema for their organizations, with various custom fields. In the context of using organization fields as a schema for defining the data fields of an organization, it must be kept in mind that some types of custom fields can have additional data fields which are not separate organization fields per se. Such is the case with monetary, daterange and timerange fields – each of these fields will have one additional data field in addition to the one presented in the context of organization fields. For example, if there is a monetary field with the key `ffk9s9` stored on the account, `ffk9s9` would hold the numeric value of the field, and `ffk9s9_currency` would hold the ISO currency code that goes along with the numeric value. To find out which data fields are available, fetch one organization and list its keys.

#### Get all organization fields

![Copy link](<Base64-Image-Removed>)

Returns data about all organization fields.

API v1

###### Cost

20

###### Request

GET

/v1/organizationFields

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

#### Get one organization field

![Copy link](<Base64-Image-Removed>)

Returns data about a specific organization field.

API v1

###### Cost

2

###### Request

GET

/v1/organizationFields/{id}

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

#### Add a new organization field

![Copy link](<Base64-Image-Removed>)

Adds a new organization field. For more information, see the tutorial for [adding a new custom field](https://pipedrive.readme.io/docs/adding-a-new-custom-field).

API v1

###### Cost

10

###### Request

POST

/v1/organizationFields

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

#### Update an organization field

![Copy link](<Base64-Image-Removed>)

Updates an organization field. For more information, see the tutorial for [updating custom fields' values](https://pipedrive.readme.io/docs/updating-custom-field-value).

API v1

###### Cost

10

###### Request

PUT

/v1/organizationFields/{id}

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

#### Delete multiple organization fields in bulk

![Copy link](<Base64-Image-Removed>)

Marks multiple fields as deleted.

API v1

###### Cost

10

###### Request

DELETE

/v1/organizationFields

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

#### Delete an organization field

![Copy link](<Base64-Image-Removed>)

Marks a field as deleted. For more information, see the tutorial for [deleting a custom field](https://pipedrive.readme.io/docs/deleting-a-custom-field).

API v1

###### Cost

6

###### Request

DELETE

/v1/organizationFields/{id}

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

Cookies Button

This website uses cookies and other tracking technologies to enhance user experience and to analyze performance and traffic on our website. We also share information about your use of our site with our social media, advertising and analytics partners. Further information is available in our: [Cookie Notice](https://www.pipedrive.com/en/cookie-notice) [Privacy Notice](https://www.pipedrive.com/en/privacy)

Continue

![Company Logo](https://cdn.cookielaw.org/logos/93bc8daa-5b3a-4f92-bef0-2fbea0b508b4/6e1288c1-32b6-4bd1-9da3-a1d3837e2da6/db1a64a6-ff95-40e1-bd8a-7cb0381253cd/Pipedrive_Logo_Green.png)

## Preference center

When you visit our website, we store cookies on your browser to collect information. The information collected might relate to you, your preferences or your device, and is mostly used to make the site work as you expect it to and to provide a more personalized web experience. However, you can choose not to allow certain types of cookies, which may impact your experience of the site and the services we are able to offer. Click on the different category headings to find out more and change our default settings according to your preference. You cannot opt-out of our First Party Strictly Necessary Cookies as they are deployed in order to ensure the proper functioning of our website (such as prompting the cookie banner and remembering your settings, to log into your account, to redirect you when you log out, etc.). For more information about the First and Third Party Cookies used please follow this link.


[Cookie Notice](https://www.pipedrive.com/en/cookie-notice) [Privacy Notice](https://www.pipedrive.com/en/privacy)

Allow All

### Manage Consent Preferences

#### Strictly Necessary Cookies

Always Active

These cookies are necessary for the website to function and cannot be switched off in our systems. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, logging in or filling in forms. You can set your browser to block or alert you about these cookies, but some parts of the site will not then work. These cookies do not store any personally identifiable information.

#### Functional Cookies

Always Active

These cookies enable the website to provide enhanced functionality and personalisation. They may be set by us or by third party providers whose services we have added to our pages.    If you do not allow these cookies then some or all of these services may not function properly.

#### Performance Cookies

Always Active

These cookies allow us to count visits and traffic sources so we can measure and improve the performance of our site. They help us to know which pages are the most and least popular and see how visitors move around the site.    All information these cookies collect is aggregated and therefore anonymous. If you do not allow these cookies we will not know when you have visited our site, and will not be able to monitor its performance.

#### Targeting Cookies

Always Active

These cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant adverts on other sites.    They do not store directly personal information, but are based on uniquely identifying your browser and internet device. If you do not allow these cookies, you will experience less targeted advertising.

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

Confirm My Choices

[![Powered by Onetrust](https://cdn.cookielaw.org/logos/static/powered_by_logo.svg)](https://www.onetrust.com/products/cookie-consent/)