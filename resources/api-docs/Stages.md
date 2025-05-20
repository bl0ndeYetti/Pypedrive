---
url: "https://developers.pipedrive.com/docs/api/v1/Stages"
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

[Pipelines](https://developers.pipedrive.com/docs/api/v1/Pipelines)

[Products](https://developers.pipedrive.com/docs/api/v1/Products)

[ProductFields](https://developers.pipedrive.com/docs/api/v1/ProductFields)

[Projects](https://developers.pipedrive.com/docs/api/v1/Projects)

[ProjectTemplates](https://developers.pipedrive.com/docs/api/v1/ProjectTemplates)

[Recents](https://developers.pipedrive.com/docs/api/v1/Recents)

[Roles](https://developers.pipedrive.com/docs/api/v1/Roles)

[Stages](https://developers.pipedrive.com/docs/api/v1/Stages)

[GET\\
\\
Get all stages](https://developers.pipedrive.com/docs/api/v1/Stages#getStages)

[GET\\
\\
Get one stage](https://developers.pipedrive.com/docs/api/v1/Stages#getStage)

[GET\\
\\
Get deals in a stage](https://developers.pipedrive.com/docs/api/v1/Stages#getStageDeals)

[POST\\
\\
Add a new stage](https://developers.pipedrive.com/docs/api/v1/Stages#addStage)

[PATCH\\
\\
Update stage details](https://developers.pipedrive.com/docs/api/v1/Stages#updateStage)

[DELETE\\
\\
Delete multiple stages in bulk](https://developers.pipedrive.com/docs/api/v1/Stages#deleteStages)

[DELETE\\
\\
Delete a stage](https://developers.pipedrive.com/docs/api/v1/Stages#deleteStage)

[Subscriptions](https://developers.pipedrive.com/docs/api/v1/Subscriptions)

[Tasks](https://developers.pipedrive.com/docs/api/v1/Tasks)

[Users](https://developers.pipedrive.com/docs/api/v1/Users)

[UserConnections](https://developers.pipedrive.com/docs/api/v1/UserConnections)

[UserSettings](https://developers.pipedrive.com/docs/api/v1/UserSettings)

[Webhooks](https://developers.pipedrive.com/docs/api/v1/Webhooks)

## Stages

Run in Postman

Stage is a logical component of a pipeline, and essentially a bucket that can hold a number of deals. In the context of the pipeline a stage belongs to, it has an order number which defines the order of stages in that pipeline.

#### Get all stages

![Copy link](<Base64-Image-Removed>)

Returns data about all stages.

[View quick guide: /v1 to /v2 migration](https://pipedrive.readme.io/docs/pipedrive-api-v2-migration-guide)

API v1

API v2

###### Cost

5

###### Request

GET

/api/v2/stages

###### Query parameters

pipeline\_id

integer

The ID of the pipeline to fetch stages for. If omitted, stages for all pipelines will be fetched.

sort\_by

string

The field to sort by. Supported fields: `id`, `update_time`, `add_time`, `order_nr`.

Default

id

Values

id

update\_time

add\_time

order\_nr

sort\_direction

string

The sorting direction. Supported values: `asc`, `desc`.

Default

asc

Values

asc

desc

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

#### Get one stage

![Copy link](<Base64-Image-Removed>)

Returns data about a specific stage.

[View quick guide: /v1 to /v2 migration](https://pipedrive.readme.io/docs/pipedrive-api-v2-migration-guide)

API v1

API v2

###### Cost

1

###### Request

GET

/api/v2/stages/{id}

###### Path parameters

id

integer

required

The ID of the stage

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }

#### Get deals in a stage

![Copy link](<Base64-Image-Removed>)

Lists deals in a specific stage. If no parameters are provided open deals owned by the authorized user will be returned.

This endpoint has been deprecated. Please use [GET /api/v2/deals?stage\_id={id}](https://developers.pipedrive.com/docs/api/v1/Deals#getDeals) instead.

Deprecated endpoint

###### Cost

20

###### Request

GET

/v1/stages/{id}/deals

###### Path parameters

id

integer

required

The ID of the stage

###### Query parameters

filter\_id

integer

If supplied, only deals matching the given filter will be returned

user\_id

integer

If supplied, `filter_id` will not be considered and only deals owned by the given user will be returned. If omitted, deals owned by the authorized user will be returned.

everyone

number

If supplied, `filter_id` and `user_id` will not be considered – instead, deals owned by everyone will be returned

Values

0

1

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

#### Add a new stage

![Copy link](<Base64-Image-Removed>)

Adds a new stage, returns the ID upon success.

[View quick guide: /v1 to /v2 migration](https://pipedrive.readme.io/docs/pipedrive-api-v2-migration-guide)

API v1

API v2

###### Cost

5

###### Request

POST

/api/v2/stages

###### Body parameters

application/json

name

string

required

The name of the stage

pipeline\_id

integer

required

The ID of the pipeline to add stage to

deal\_probability

integer

The success probability percentage of the deal. Used/shown when deal weighted values are used.

is\_deal\_rot\_enabled

boolean

Whether deals in this stage can become rotten

days\_to\_rotten

integer

The number of days the deals not updated in this stage would become rotten. Applies only if the `is_deal_rot_enabled` is set.

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }

#### Update stage details

![Copy link](<Base64-Image-Removed>)

Updates the properties of a stage.

[View quick guide: /v1 to /v2 migration](https://pipedrive.readme.io/docs/pipedrive-api-v2-migration-guide)

API v1

API v2

###### Cost

5

###### Request

PATCH

/api/v2/stages/{id}

###### Path parameters

id

integer

required

The ID of the stage

###### Body parameters

application/json

name

string

The name of the stage

pipeline\_id

integer

The ID of the pipeline to add stage to

deal\_probability

integer

The success probability percentage of the deal. Used/shown when deal weighted values are used.

is\_deal\_rot\_enabled

boolean

Whether deals in this stage can become rotten

days\_to\_rotten

integer

The number of days the deals not updated in this stage would become rotten. Applies only if the `is_deal_rot_enabled` is set.

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }

#### Delete multiple stages in bulk

![Copy link](<Base64-Image-Removed>)

Marks multiple stages as deleted.

This endpoint has been deprecated. Please use [DELETE /api/v2/stages/{id}](https://developers.pipedrive.com/docs/api/v1/Stages#deleteStage) instead.

Deprecated endpoint

###### Cost

10

###### Request

DELETE

/v1/stages

###### Query parameters

ids

string

required

The comma-separated stage IDs to delete

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }

#### Delete a stage

![Copy link](<Base64-Image-Removed>)

Marks a stage as deleted.

[View quick guide: /v1 to /v2 migration](https://pipedrive.readme.io/docs/pipedrive-api-v2-migration-guide)

API v1

API v2

###### Cost

3

###### Request

DELETE

/api/v2/stages/{id}

###### Path parameters

id

integer

required

The ID of the stage

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