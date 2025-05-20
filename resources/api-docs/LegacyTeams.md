---
url: "https://developers.pipedrive.com/docs/api/v1/LegacyTeams"
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

[GET\\
\\
Get all teams](https://developers.pipedrive.com/docs/api/v1/LegacyTeams#getTeams)

[GET\\
\\
Get a single team](https://developers.pipedrive.com/docs/api/v1/LegacyTeams#getTeam)

[GET\\
\\
Get all users in a team](https://developers.pipedrive.com/docs/api/v1/LegacyTeams#getTeamUsers)

[GET\\
\\
Get all teams of a user](https://developers.pipedrive.com/docs/api/v1/LegacyTeams#getUserTeams)

[POST\\
\\
Add a new team](https://developers.pipedrive.com/docs/api/v1/LegacyTeams#addTeam)

[POST\\
\\
Add users to a team](https://developers.pipedrive.com/docs/api/v1/LegacyTeams#addTeamUser)

[PUT\\
\\
Update a team](https://developers.pipedrive.com/docs/api/v1/LegacyTeams#updateTeam)

[DELETE\\
\\
Delete users from a team](https://developers.pipedrive.com/docs/api/v1/LegacyTeams#deleteTeamUser)

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

## LegacyTeams

Run in Postman

Legacy teams allow you to form groups of users withing the organization for more efficient management. Previously Legacy Teams were called Teams and occupied the `v1/teams*` path. They're being deprecated because we are preparing for an upgraded version of the Teams API, which requires migrating the current functionality to a new path URL `v1/legacyTeams*`. The functionality and [OAuth scopes](https://pipedrive.readme.io/docs/marketplace-scopes-and-permissions-explanations) of all the Teams API endpoints will remain the same.

#### Get all teams

![Copy link](<Base64-Image-Removed>)

Returns data about teams within the company.

Deprecated endpoint

###### Cost

20

###### Request

GET

/v1/legacyTeams

###### Query parameters

order\_by

string

The field name to sort returned teams by

Default

id

Values

id

name

manager\_id

active\_flag

skip\_users

number

When enabled, the teams will not include IDs of member users

Default

0

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

#### Get a single team

![Copy link](<Base64-Image-Removed>)

Returns data about a specific team.

Deprecated endpoint

###### Cost

2

###### Request

GET

/v1/legacyTeams/{id}

###### Path parameters

id

integer

required

The ID of the team

###### Query parameters

skip\_users

number

When enabled, the teams will not include IDs of member users

Default

0

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


"data":{ ... }

#### Get all users in a team

![Copy link](<Base64-Image-Removed>)

Returns a list of all user IDs within a team.

Deprecated endpoint

###### Cost

20

###### Request

GET

/v1/legacyTeams/{id}/users

###### Path parameters

id

integer

required

The ID of the team

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":\[ ... \]

#### Get all teams of a user

![Copy link](<Base64-Image-Removed>)

Returns data about all teams which have the specified user as a member.

Deprecated endpoint

###### Cost

20

###### Request

GET

/v1/legacyTeams/user/{id}

###### Path parameters

id

integer

required

The ID of the user

###### Query parameters

order\_by

string

The field name to sort returned teams by

Default

id

Values

id

name

manager\_id

active\_flag

skip\_users

number

When enabled, the teams will not include IDs of member users

Default

0

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

#### Add a new team

![Copy link](<Base64-Image-Removed>)

Adds a new team to the company and returns the created object.

Deprecated endpoint

###### Cost

10

###### Request

POST

/v1/legacyTeams

###### Body parameters

application/json

name

string

required

The team name

description

string

The team description

manager\_id

integer

required

The team manager ID

users

array

The list of user IDs

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }

#### Add users to a team

![Copy link](<Base64-Image-Removed>)

Adds users to an existing team.

Deprecated endpoint

###### Cost

10

###### Request

POST

/v1/legacyTeams/{id}/users

###### Path parameters

id

integer

required

The ID of the team

###### Body parameters

application/json

users

array

required

The list of user IDs

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":\[ ... \]

#### Update a team

![Copy link](<Base64-Image-Removed>)

Updates an existing team and returns the updated object.

Deprecated endpoint

###### Cost

10

###### Request

PUT

/v1/legacyTeams/{id}

###### Path parameters

id

integer

required

The ID of the team

###### Body parameters

application/json

name

string

The team name

description

string

The team description

manager\_id

integer

The team manager ID

users

array

The list of user IDs

active\_flag

Flag that indicates whether the team is active

Values

0

1

deleted\_flag

Flag that indicates whether the team is deleted

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


"data":{ ... }

#### Delete users from a team

![Copy link](<Base64-Image-Removed>)

Deletes users from an existing team.

Deprecated endpoint

###### Cost

10

###### Request

DELETE

/v1/legacyTeams/{id}/users

###### Path parameters

id

integer

required

The ID of the team

###### Body parameters

application/json

users

array

required

The list of user IDs

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":\[ ... \]

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