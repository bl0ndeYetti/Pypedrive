---
url: "https://developers.pipedrive.com/docs/api/v1/Activities"
title: "Pipedrive API Reference and Documentation"
---

API Reference

###### API Reference

[Getting started](https://developers.pipedrive.com/docs/api/v1)

###### Endpoints

[Activities](https://developers.pipedrive.com/docs/api/v1/Activities)

[GET\\
\\
Get all activities assigned to a particular user](https://developers.pipedrive.com/docs/api/v1/Activities#getActivities)

[GET\\
\\
Get all activities collection](https://developers.pipedrive.com/docs/api/v1/Activities#getActivitiesCollection)

[GET\\
\\
Get details of an activity](https://developers.pipedrive.com/docs/api/v1/Activities#getActivity)

[POST\\
\\
Add an activity](https://developers.pipedrive.com/docs/api/v1/Activities#addActivity)

[PATCH\\
\\
Update an activity](https://developers.pipedrive.com/docs/api/v1/Activities#updateActivity)

[DELETE\\
\\
Delete multiple activities in bulk](https://developers.pipedrive.com/docs/api/v1/Activities#deleteActivities)

[DELETE\\
\\
Delete an activity](https://developers.pipedrive.com/docs/api/v1/Activities#deleteActivity)

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

[Subscriptions](https://developers.pipedrive.com/docs/api/v1/Subscriptions)

[Tasks](https://developers.pipedrive.com/docs/api/v1/Tasks)

[Users](https://developers.pipedrive.com/docs/api/v1/Users)

[UserConnections](https://developers.pipedrive.com/docs/api/v1/UserConnections)

[UserSettings](https://developers.pipedrive.com/docs/api/v1/UserSettings)

[Webhooks](https://developers.pipedrive.com/docs/api/v1/Webhooks)

## Activities

Run in Postman

Activities are appointments/tasks/events on a calendar that can be associated with a deal, a lead, a person and an organization. Activities can be of different type (such as call, meeting, lunch or a custom type - see ActivityTypes object) and can be assigned to a particular user. Note that activities can also be created without a specific date/time.

#### Get all activities assigned to a particular user

![Copy link](<Base64-Image-Removed>)

Returns data about all activities.

[View quick guide: /v1 to /v2 migration](https://pipedrive.readme.io/docs/pipedrive-api-v2-migration-guide)

API v1

API v2

###### Cost

10

###### Request

GET

/api/v2/activities

###### Query parameters

filter\_id

integer

If supplied, only activities matching the specified filter are returned

ids

string

Optional comma separated string array of up to 100 entity ids to fetch. If filter\_id is provided, this is ignored. If any of the requested entities do not exist or are not visible, they are not included in the response.

owner\_id

integer

If supplied, only activities owned by the specified user are returned. If filter\_id is provided, this is ignored.

deal\_id

integer

If supplied, only activities linked to the specified deal are returned. If filter\_id is provided, this is ignored.

lead\_id

string

If supplied, only activities linked to the specified lead are returned. If filter\_id is provided, this is ignored.

person\_id

integer

If supplied, only activities whose primary participant is the given person are returned. If filter\_id is provided, this is ignored.

org\_id

integer

If supplied, only activities linked to the specified organization are returned. If filter\_id is provided, this is ignored.

done

boolean

If supplied, only activities with specified 'done' flag value are returned

updated\_since

string

If set, only activities with an `update_time` later than or equal to this time are returned. In RFC3339 format, e.g. 2025-01-01T10:20:00Z.

updated\_until

string

If set, only activities with an `update_time` earlier than this time are returned. In RFC3339 format, e.g. 2025-01-01T10:20:00Z.

sort\_by

string

The field to sort by. Supported fields: `id`, `update_time`, `add_time`, `due_date`.

Default

id

Values

id

update\_time

add\_time

due\_date

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

attendees

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

#### Get all activities collection

![Copy link](<Base64-Image-Removed>)

Returns all activities. Please note that only global admins (those with global permissions) can access this endpoint. Users with regular permissions will receive a 403 response. Read more about global permissions [here](https://support.pipedrive.com/en/article/global-user-management).

This endpoint has been deprecated. Please use [GET /api/v2/activities](https://developers.pipedrive.com/docs/api/v1/Activities#getActivities) instead.

Deprecated endpoint

###### Cost

10

###### Request

GET

/v1/activities/collection

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

user\_id

integer

The ID of the user whose activities will be fetched. If omitted, all activities are returned.

done

boolean

Whether the activity is done or not. `false` = Not done, `true` = Done. If omitted, returns both done and not done activities.

type

string

The type of the activity, can be one type or multiple types separated by a comma. This is in correlation with the `key_string` parameter of ActivityTypes.

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

#### Get details of an activity

![Copy link](<Base64-Image-Removed>)

Returns the details of a specific activity.

[View quick guide: /v1 to /v2 migration](https://pipedrive.readme.io/docs/pipedrive-api-v2-migration-guide)

API v1

API v2

###### Cost

1

###### Request

GET

/api/v2/activities/{id}

###### Path parameters

id

integer

required

The ID of the activity

###### Query parameters

include\_fields

string

Optional comma separated string array of additional fields to include

Values

attendees

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }

#### Add an activity

![Copy link](<Base64-Image-Removed>)

Adds a new activity.

[View quick guide: /v1 to /v2 migration](https://pipedrive.readme.io/docs/pipedrive-api-v2-migration-guide)

API v1

API v2

###### Cost

5

###### Request

POST

/api/v2/activities

###### Body parameters

application/json

subject

string

The subject of the activity

type

string

The type of the activity

owner\_id

integer

The ID of the user who owns the activity

deal\_id

integer

The ID of the deal linked to the activity

lead\_id

string

The ID of the lead linked to the activity

person\_id

integer

The ID of the person linked to the activity

org\_id

integer

The ID of the organization linked to the activity

project\_id

integer

The ID of the project linked to the activity

due\_date

string

The due date of the activity

due\_time

string

The due time of the activity

duration

string

The duration of the activity

busy

boolean

Whether the activity marks the assignee as busy or not in their calendar

done

boolean

Whether the activity is marked as done or not

location

object

Location of the activity

participants

array

The participants of the activity

attendees

array

The attendees of the activity

public\_description

string

The public description of the activity

priority

integer

The priority of the activity. Mappable to a specific string using activityFields API.

note

string

The note of the activity

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }

#### Update an activity

![Copy link](<Base64-Image-Removed>)

Updates the properties of an activity.

[View quick guide: /v1 to /v2 migration](https://pipedrive.readme.io/docs/pipedrive-api-v2-migration-guide)

API v1

API v2

###### Cost

5

###### Request

PATCH

/api/v2/activities/{id}

###### Path parameters

id

integer

required

The ID of the activity

###### Body parameters

application/json

subject

string

The subject of the activity

type

string

The type of the activity

owner\_id

integer

The ID of the user who owns the activity

deal\_id

integer

The ID of the deal linked to the activity

lead\_id

string

The ID of the lead linked to the activity

person\_id

integer

The ID of the person linked to the activity

org\_id

integer

The ID of the organization linked to the activity

project\_id

integer

The ID of the project linked to the activity

due\_date

string

The due date of the activity

due\_time

string

The due time of the activity

duration

string

The duration of the activity

busy

boolean

Whether the activity marks the assignee as busy or not in their calendar

done

boolean

Whether the activity is marked as done or not

location

object

Location of the activity

participants

array

The participants of the activity

attendees

array

The attendees of the activity

public\_description

string

The public description of the activity

priority

integer

The priority of the activity. Mappable to a specific string using activityFields API.

note

string

The note of the activity

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }

#### Delete multiple activities in bulk

![Copy link](<Base64-Image-Removed>)

Marks multiple activities as deleted. After 30 days, the activities will be permanently deleted.

This endpoint has been deprecated. Please use [DELETE /api/v2/activities/{id}](https://developers.pipedrive.com/docs/api/v1/Activities#deleteActivity) instead.

Deprecated endpoint

###### Cost

10

###### Request

DELETE

/v1/activities

###### Query parameters

ids

string

required

The comma-separated IDs of activities that will be deleted

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }

#### Delete an activity

![Copy link](<Base64-Image-Removed>)

Marks an activity as deleted. After 30 days, the activity will be permanently deleted.

[View quick guide: /v1 to /v2 migration](https://pipedrive.readme.io/docs/pipedrive-api-v2-migration-guide)

API v1

API v2

###### Cost

3

###### Request

DELETE

/api/v2/activities/{id}

###### Path parameters

id

integer

required

The ID of the activity

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