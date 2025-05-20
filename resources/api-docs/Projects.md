---
url: "https://developers.pipedrive.com/docs/api/v1/Projects"
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

[GET\\
\\
Get all projects](https://developers.pipedrive.com/docs/api/v1/Projects#getProjects)

[GET\\
\\
Get details of a project](https://developers.pipedrive.com/docs/api/v1/Projects#getProject)

[GET\\
\\
Returns project plan](https://developers.pipedrive.com/docs/api/v1/Projects#getProjectPlan)

[GET\\
\\
Returns project groups](https://developers.pipedrive.com/docs/api/v1/Projects#getProjectGroups)

[GET\\
\\
Returns project tasks](https://developers.pipedrive.com/docs/api/v1/Projects#getProjectTasks)

[GET\\
\\
Returns project activities](https://developers.pipedrive.com/docs/api/v1/Projects#getProjectActivities)

[GET\\
\\
Get all project boards](https://developers.pipedrive.com/docs/api/v1/Projects#getProjectsBoards)

[GET\\
\\
Get details of a board](https://developers.pipedrive.com/docs/api/v1/Projects#getProjectsBoard)

[GET\\
\\
Get project phases](https://developers.pipedrive.com/docs/api/v1/Projects#getProjectsPhases)

[GET\\
\\
Get details of a phase](https://developers.pipedrive.com/docs/api/v1/Projects#getProjectsPhase)

[POST\\
\\
Add a project](https://developers.pipedrive.com/docs/api/v1/Projects#addProject)

[POST\\
\\
Archive a project](https://developers.pipedrive.com/docs/api/v1/Projects#archiveProject)

[PUT\\
\\
Update a project](https://developers.pipedrive.com/docs/api/v1/Projects#updateProject)

[PUT\\
\\
Update activity in project plan](https://developers.pipedrive.com/docs/api/v1/Projects#putProjectPlanActivity)

[PUT\\
\\
Update task in project plan](https://developers.pipedrive.com/docs/api/v1/Projects#putProjectPlanTask)

[DELETE\\
\\
Delete a project](https://developers.pipedrive.com/docs/api/v1/Projects#deleteProject)

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

## Projects

Run in Postman

Projects represent ongoing, completed or canceled projects attached to an organization, person or to deals. Each project has an owner and must be placed in a phase. Each project consists of standard data fields but can also contain a number of custom fields. The custom fields can be recognized by long hashes as keys.

#### Get all projects

![Copy link](<Base64-Image-Removed>)

Returns all projects. This is a cursor-paginated endpoint. For more information, please refer to our documentation on [pagination](https://pipedrive.readme.io/docs/core-api-concepts-pagination).

API v1

###### Cost

20

###### Request

GET

/v1/projects

###### Query parameters

cursor

string

For pagination, the marker (an opaque string value) representing the first item on the next page

limit

integer

For pagination, the limit of entries to be returned. If not provided, 100 items will be returned.

filter\_id

integer

The ID of the filter to use

status

string

If supplied, includes only projects with the specified statuses. Possible values are `open`, `completed`, `canceled` and `deleted`. By default `deleted` projects are not returned.

phase\_id

integer

If supplied, only projects in specified phase are returned

include\_archived

boolean

If supplied with `true` then archived projects are also included in the response. By default only not archived projects are returned.

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

#### Get details of a project

![Copy link](<Base64-Image-Removed>)

Returns the details of a specific project. Also note that custom fields appear as long hashes in the resulting data. These hashes can be mapped against the `key` value of project fields.

API v1

###### Cost

2

###### Request

GET

/v1/projects/{id}

###### Path parameters

id

integer

required

The ID of the project

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }
- "additional\_data":null

#### Returns project plan

![Copy link](<Base64-Image-Removed>)

Returns information about items in a project plan. Items consists of tasks and activities and are linked to specific project phase and group.

API v1

###### Cost

20

###### Request

GET

/v1/projects/{id}/plan

###### Path parameters

id

integer

required

The ID of the project

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":\[ ... \]
- "additional\_data":null

#### Returns project groups

![Copy link](<Base64-Image-Removed>)

Returns all active groups under a specific project.

API v1

###### Cost

20

###### Request

GET

/v1/projects/{id}/groups

###### Path parameters

id

integer

required

The ID of the project

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":\[ ... \]
- "additional\_data":null

#### Returns project tasks

![Copy link](<Base64-Image-Removed>)

Returns tasks linked to a specific project.

API v1

###### Cost

20

###### Request

GET

/v1/projects/{id}/tasks

###### Path parameters

id

integer

required

The ID of the project

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

#### Returns project activities

![Copy link](<Base64-Image-Removed>)

Returns activities linked to a specific project.

API v1

###### Cost

20

###### Request

GET

/v1/projects/{id}/activities

###### Path parameters

id

integer

required

The ID of the project

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

#### Get all project boards

![Copy link](<Base64-Image-Removed>)

Returns all projects boards that are not deleted.

API v1

###### Cost

20

###### Request

GET

/v1/projects/boards

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":\[ ... \]
- "additional\_data":null

#### Get details of a board

![Copy link](<Base64-Image-Removed>)

Returns the details of a specific project board.

API v1

###### Cost

2

###### Request

GET

/v1/projects/boards/{id}

###### Path parameters

id

integer

required

The ID of the project board

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }
- "additional\_data":null

#### Get project phases

![Copy link](<Base64-Image-Removed>)

Returns all active project phases under a specific board.

API v1

###### Cost

20

###### Request

GET

/v1/projects/phases

###### Query parameters

board\_id

integer

required

ID of the board for which phases are requested

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":\[ ... \]
- "additional\_data":null

#### Get details of a phase

![Copy link](<Base64-Image-Removed>)

Returns the details of a specific project phase.

API v1

###### Cost

2

###### Request

GET

/v1/projects/phases/{id}

###### Path parameters

id

integer

required

The ID of the project phase

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }
- "additional\_data":null

#### Add a project

![Copy link](<Base64-Image-Removed>)

Adds a new project. Note that you can supply additional custom fields along with the request that are not described here. These custom fields are different for each Pipedrive account and can be recognized by long hashes as keys.

API v1

###### Cost

10

###### Request

POST

/v1/projects

###### Body parameters

application/json

title

string

required

The title of the project

board\_id

number

required

The ID of a project board

phase\_id

number

required

The ID of a phase on a project board

description

string

The description of the project

status

string

The status of the project

owner\_id

number

The ID of a project owner

start\_date

string

The start date of the project. Format: YYYY-MM-DD.

Format

date

end\_date

string

The end date of the project. Format: YYYY-MM-DD.

Format

date

deal\_ids

array

An array of IDs of the deals this project is associated with

org\_id

number

The ID of the organization this project is associated with

person\_id

number

The ID of the person this project is associated with

labels

array

An array of IDs of the labels this project has

template\_id

number

The ID of the template the project will be based on

###### Response

201

Created

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }
- "additional\_data":null

#### Archive a project

![Copy link](<Base64-Image-Removed>)

Archives a project.

API v1

###### Cost

10

###### Request

POST

/v1/projects/{id}/archive

###### Path parameters

id

integer

required

The ID of the project

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }
- "additional\_data":null

#### Update a project

![Copy link](<Base64-Image-Removed>)

Updates a project.

API v1

###### Cost

10

###### Request

PUT

/v1/projects/{id}

###### Path parameters

id

integer

required

The ID of the project

###### Body parameters

application/json

title

string

The title of the project

board\_id

number

The ID of the board this project is associated with

phase\_id

number

The ID of the phase this project is associated with

description

string

The description of the project

status

string

The status of the project

owner\_id

number

The ID of a project owner

start\_date

string

The start date of the project. Format: YYYY-MM-DD.

Format

date

end\_date

string

The end date of the project. Format: YYYY-MM-DD.

Format

date

deal\_ids

array

An array of IDs of the deals this project is associated with

org\_id

number

The ID of the organization this project is associated with

person\_id

number

The ID of the person this project is associated with

labels

array

An array of IDs of the labels this project has

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }
- "additional\_data":null

#### Update activity in project plan

![Copy link](<Base64-Image-Removed>)

Updates an activity phase or group in a project.

API v1

###### Cost

10

###### Request

PUT

/v1/projects/{id}/plan/activities/{activityId}

###### Path parameters

id

integer

required

The ID of the project

activityId

integer

required

The ID of the activity

###### Body parameters

application/json

phase\_id

number

The ID of a phase on a project board

group\_id

number

The ID of a group on a project board

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }
- "additional\_data":null

#### Update task in project plan

![Copy link](<Base64-Image-Removed>)

Updates a task phase or group in a project.

API v1

###### Cost

10

###### Request

PUT

/v1/projects/{id}/plan/tasks/{taskId}

###### Path parameters

id

integer

required

The ID of the project

taskId

integer

required

The ID of the task

###### Body parameters

application/json

phase\_id

number

The ID of a phase on a project board

group\_id

number

The ID of a group on a project board

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }
- "additional\_data":null

#### Delete a project

![Copy link](<Base64-Image-Removed>)

Marks a project as deleted.

API v1

###### Cost

6

###### Request

DELETE

/v1/projects/{id}

###### Path parameters

id

integer

required

The ID of the project

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }
- "additional\_data":null

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