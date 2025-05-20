---
url: "https://developers.pipedrive.com/docs/api/v1/Users"
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

[Subscriptions](https://developers.pipedrive.com/docs/api/v1/Subscriptions)

[Tasks](https://developers.pipedrive.com/docs/api/v1/Tasks)

[Users](https://developers.pipedrive.com/docs/api/v1/Users)

[GET\\
\\
Get all users](https://developers.pipedrive.com/docs/api/v1/Users#getUsers)

[GET\\
\\
Find users by name](https://developers.pipedrive.com/docs/api/v1/Users#findUsersByName)

[GET\\
\\
Get current user data](https://developers.pipedrive.com/docs/api/v1/Users#getCurrentUser)

[GET\\
\\
Get one user](https://developers.pipedrive.com/docs/api/v1/Users#getUser)

[GET\\
\\
List followers of a user](https://developers.pipedrive.com/docs/api/v1/Users#getUserFollowers)

[GET\\
\\
List user permissions](https://developers.pipedrive.com/docs/api/v1/Users#getUserPermissions)

[GET\\
\\
List role assignments](https://developers.pipedrive.com/docs/api/v1/Users#getUserRoleAssignments)

[GET\\
\\
List user role settings](https://developers.pipedrive.com/docs/api/v1/Users#getUserRoleSettings)

[POST\\
\\
Add a new user](https://developers.pipedrive.com/docs/api/v1/Users#addUser)

[PUT\\
\\
Update user details](https://developers.pipedrive.com/docs/api/v1/Users#updateUser)

[UserConnections](https://developers.pipedrive.com/docs/api/v1/UserConnections)

[UserSettings](https://developers.pipedrive.com/docs/api/v1/UserSettings)

[Webhooks](https://developers.pipedrive.com/docs/api/v1/Webhooks)

## Users

Run in Postman

Users are people with access to your Pipedrive account. A user may belong to one or many Pipedrive accounts, so deleting a user from one Pipedrive account will not remove the user from the data store if he/she is connected to multiple accounts. Users should not be confused with persons.

#### Get all users

![Copy link](<Base64-Image-Removed>)

Returns data about all users within the company.

API v1

###### Cost

20

###### Request

GET

/v1/users

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":\[ ... \]

#### Find users by name

![Copy link](<Base64-Image-Removed>)

Finds users by their name.

API v1

###### Cost

40

###### Request

GET

/v1/users/find

###### Query parameters

term

string

required

The search term to look for

search\_by\_email

number

When enabled, the term will only be matched against email addresses of users. Default: `false`.

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

#### Get current user data

![Copy link](<Base64-Image-Removed>)

Returns data about an authorized user within the company with bound company data: company ID, company name, and domain. Note that the `locale` property means 'Date/number format' in the Pipedrive account settings, not the chosen language.

API v1

###### Cost

2

###### Request

GET

/v1/users/me

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }

#### Get one user

![Copy link](<Base64-Image-Removed>)

Returns data about a specific user within the company.

API v1

###### Cost

2

###### Request

GET

/v1/users/{id}

###### Path parameters

id

integer

required

The ID of the user

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }

#### List followers of a user

![Copy link](<Base64-Image-Removed>)

Lists users who are following the user.

[View quick guide: /v1 to /v2 migration](https://pipedrive.readme.io/docs/pipedrive-api-v2-migration-guide)

API v1

API v2

###### Cost

10

###### Request

GET

/api/v2/users/{id}/followers

###### Path parameters

id

integer

required

The ID of the user

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

#### List user permissions

![Copy link](<Base64-Image-Removed>)

Lists aggregated permissions over all assigned permission sets for a user.

API v1

###### Cost

10

###### Request

GET

/v1/users/{id}/permissions

###### Path parameters

id

integer

required

The ID of the user

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }

#### List role assignments

![Copy link](<Base64-Image-Removed>)

Lists role assignments for a user.

API v1

###### Cost

10

###### Request

GET

/v1/users/{id}/roleAssignments

###### Path parameters

id

integer

required

The ID of the user

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

#### List user role settings

![Copy link](<Base64-Image-Removed>)

Lists the settings of user's assigned role.

API v1

###### Cost

10

###### Request

GET

/v1/users/{id}/roleSettings

###### Path parameters

id

integer

required

The ID of the user

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }

#### Add a new user

![Copy link](<Base64-Image-Removed>)

Adds a new user to the company, returns the ID upon success.

API v1

###### Cost

10

###### Request

POST

/v1/users

###### Body parameters

application/json

email

string

required

The email of the user

access

array

The access given to the user. Each item in the array represents access to a specific app. Optionally may include either admin flag or permission set ID to specify which access to give within the app. If both are omitted, the default access for the corresponding app will be used. It requires structure as follows: `[{ app: 'sales', permission_set_id: '62cc4d7f-4038-4352-abf3-a8c1c822b631' }, { app: 'global', admin: true }, { app: 'account_settings' }]`

Default

\[object Object\]

active\_flag

boolean

Whether the user is active or not. `false` = Not activated, `true` = Activated

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

#### Update user details

![Copy link](<Base64-Image-Removed>)

Updates the properties of a user. Currently, only `active_flag` can be updated.

API v1

###### Cost

10

###### Request

PUT

/v1/users/{id}

###### Path parameters

id

integer

required

The ID of the user

###### Body parameters

application/json

active\_flag

boolean

required

Whether the user is active or not. `false` = Not activated, `true` = Activated

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