---
url: "https://developers.pipedrive.com/docs/api/v1/Goals"
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

[GET\\
\\
Find goals](https://developers.pipedrive.com/docs/api/v1/Goals#getGoals)

[GET\\
\\
Get result of a goal](https://developers.pipedrive.com/docs/api/v1/Goals#getGoalResult)

[POST\\
\\
Add a new goal](https://developers.pipedrive.com/docs/api/v1/Goals#addGoal)

[PUT\\
\\
Update existing goal](https://developers.pipedrive.com/docs/api/v1/Goals#updateGoal)

[DELETE\\
\\
Delete existing goal](https://developers.pipedrive.com/docs/api/v1/Goals#deleteGoal)

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

## Goals

Run in Postman

Goals help your team meet your sales targets. There are three types of goals - company, team and user.

#### Find goals

![Copy link](<Base64-Image-Removed>)

Returns data about goals based on criteria. For searching, append `{searchField}={searchValue}` to the URL, where `searchField` can be any one of the lowest-level fields in dot-notation (e.g. `type.params.pipeline_id`; `title`). `searchValue` should be the value you are looking for on that field. Additionally, `is_active=<true|false>` can be provided to search for only active/inactive goals. When providing `period.start`, `period.end` must also be provided and vice versa.

API v1

###### Cost

20

###### Request

GET

/v1/goals/find

###### Query parameters

type.name

string

The type of the goal. If provided, everyone's goals will be returned.

Values

deals\_won

deals\_progressed

activities\_completed

activities\_added

deals\_started

title

string

The title of the goal

is\_active

boolean

Whether the goal is active or not

Default

true

assignee.id

integer

The ID of the user who's goal to fetch. When omitted, only your goals will be returned.

assignee.type

string

The type of the goal's assignee. If provided, everyone's goals will be returned.

Values

person

company

team

expected\_outcome.target

number

The numeric value of the outcome. If provided, everyone's goals will be returned.

expected\_outcome.tracking\_metric

string

The tracking metric of the expected outcome of the goal. If provided, everyone's goals will be returned.

Values

quantity

sum

expected\_outcome.currency\_id

integer

The numeric ID of the goal's currency. Only applicable to goals with `expected_outcome.tracking_metric` with value `sum`. If provided, everyone's goals will be returned.

type.params.pipeline\_id

array

An array of pipeline IDs or `null` for all pipelines. If provided, everyone's goals will be returned.

type.params.stage\_id

integer

The ID of the stage. Applicable to only `deals_progressed` type of goals. If provided, everyone's goals will be returned.

type.params.activity\_type\_id

array

An array of IDs or `null` for all activity types. Only applicable for `activities_completed` and/or `activities_added` types of goals. If provided, everyone's goals will be returned.

period.start

string

The start date of the period for which to find goals. Date in format of YYYY-MM-DD. When `period.start` is provided, `period.end` must be provided too.

Format

date

period.end

string

The end date of the period for which to find goals. Date in format of YYYY-MM-DD.

Format

date

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- "statusCode":20000
- "statusText":"OK"
- "service":"statistics-goals-api"
- ▶


"data":{ ... }

#### Get result of a goal

![Copy link](<Base64-Image-Removed>)

Gets the progress of a goal for the specified period.

API v1

###### Cost

20

###### Request

GET

/v1/goals/{id}/results

###### Path parameters

id

string

required

The ID of the goal that the results are looked for

###### Query parameters

period.start

string

required

The start date of the period for which to find the goal's progress. Format: YYYY-MM-DD. This date must be the same or after the goal duration start date.

Format

date

period.end

string

required

The end date of the period for which to find the goal's progress. Format: YYYY-MM-DD. This date must be the same or before the goal duration end date.

Format

date

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- "statusCode":20000
- "statusText":"OK"
- "service":"statistics-goals-api"
- ▶


"data":{ ... }

#### Add a new goal

![Copy link](<Base64-Image-Removed>)

Adds a new goal. Along with adding a new goal, a report is created to track the progress of your goal.

API v1

###### Cost

10

###### Request

POST

/v1/goals

###### Body parameters

application/json

title

string

The title of the goal

assignee

object

required

Who this goal is assigned to. It requires the following JSON structure: `{ "id": "1", "type": "person" }`. `type` can be either `person`, `company` or `team`. ID of the assignee person, company or team.

type

object

required

The type of the goal. It requires the following JSON structure: `{ "name": "deals_started", "params": { "pipeline_id": [1, 2], "activity_type_id": [9] } }`. Type can be one of: `deals_won`, `deals_progressed`, `activities_completed`, `activities_added`, `deals_started` or `revenue_forecast`. `params` can include `pipeline_id`, `stage_id` or `activity_type_id`. `stage_id` is related to only `deals_progressed` type of goals and `activity_type_id` to `activities_completed` or `activities_added` types of goals. The `pipeline_id` and `activity_type_id` need to be given as an array of integers. To track the goal in all pipelines, set `pipeline_id` as `null` and similarly, to track the goal for all activities, set `activity_type_id` as `null`.”

expected\_outcome

object

required

The expected outcome of the goal. Expected outcome can be tracked either by `quantity` or by `sum`. It requires the following JSON structure: `{ "target": "50", "tracking_metric": "quantity" }` or `{ "target": "50", "tracking_metric": "sum", "currency_id": 1 }`. `currency_id` should only be added to `sum` type of goals.

duration

object

required

The date when the goal starts and ends. It requires the following JSON structure: `{ "start": "2019-01-01", "end": "2022-12-31" }`. Date in format of YYYY-MM-DD. "end" can be set to `null` for an infinite, open-ended goal.

interval

string

required

The interval of the goal

Values

weekly

monthly

quarterly

yearly

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- "statusCode":20000
- "statusText":"OK"
- "service":"statistics-goals-api"
- ▶


"data":{ ... }

#### Update existing goal

![Copy link](<Base64-Image-Removed>)

Updates an existing goal.

API v1

###### Cost

10

###### Request

PUT

/v1/goals/{id}

###### Path parameters

id

string

required

The ID of the goal

###### Body parameters

application/json

title

string

The title of the goal

assignee

object

Who this goal is assigned to. It requires the following JSON structure: `{ "id": "1", "type": "person" }`. `type` can be either `person`, `company` or `team`. ID of the assignee person, company or team.

type

object

The type of the goal. It requires the following JSON structure: `{ "name": "deals_started", "params": { "pipeline_id": [1, 2], "activity_type_id": [9] } }`. Type can be one of: `deals_won`, `deals_progressed`, `activities_completed`, `activities_added`, `deals_started` or `revenue_forecast`. `params` can include `pipeline_id`, `stage_id` or `activity_type_id`. `stage_id` is related to only `deals_progressed` type of goals and `activity_type_id` to `activities_completed` or `activities_added` types of goals. The `pipeline_id` and `activity_type_id` need to be given as an array of integers. To track the goal in all pipelines, set `pipeline_id` as `null` and similarly, to track the goal for all activities, set `activity_type_id` as `null`.”

expected\_outcome

object

The expected outcome of the goal. Expected outcome can be tracked either by `quantity` or by `sum`. It requires the following JSON structure: `{ "target": "50", "tracking_metric": "quantity" }` or `{ "target": "50", "tracking_metric": "sum", "currency_id": 1 }`. `currency_id` should only be added to `sum` type of goals.

duration

object

The date when the goal starts and ends. It requires the following JSON structure: `{ "start": "2019-01-01", "end": "2022-12-31" }`. Date in format of YYYY-MM-DD. "end" can be set to `null` for an infinite, open-ended goal.

interval

string

The interval of the goal

Values

weekly

monthly

quarterly

yearly

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- "statusCode":20000
- "statusText":"OK"
- "service":"statistics-goals-api"
- ▶


"data":{ ... }

#### Delete existing goal

![Copy link](<Base64-Image-Removed>)

Marks a goal as deleted.

API v1

###### Cost

6

###### Request

DELETE

/v1/goals/{id}

###### Path parameters

id

string

required

The ID of the goal

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- "statusCode":20000
- "statusText":"OK"
- "service":"statistics-goals-api"

### Subscribe to Pipedrive’s Developer Newsletter

Your email address

Subscribe

We promise not to send you any marketing materials or spam, just developer news.

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