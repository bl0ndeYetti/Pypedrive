---
url: "https://developers.pipedrive.com/docs/api/v1/Roles"
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

[GET\\
\\
Get all roles](https://developers.pipedrive.com/docs/api/v1/Roles#getRoles)

[GET\\
\\
Get one role](https://developers.pipedrive.com/docs/api/v1/Roles#getRole)

[GET\\
\\
List role assignments](https://developers.pipedrive.com/docs/api/v1/Roles#getRoleAssignments)

[GET\\
\\
List role settings](https://developers.pipedrive.com/docs/api/v1/Roles#getRoleSettings)

[GET\\
\\
List pipeline visibility for a role](https://developers.pipedrive.com/docs/api/v1/Roles#getRolePipelines)

[POST\\
\\
Add a role](https://developers.pipedrive.com/docs/api/v1/Roles#addRole)

[POST\\
\\
Add role assignment](https://developers.pipedrive.com/docs/api/v1/Roles#addRoleAssignment)

[POST\\
\\
Add or update role setting](https://developers.pipedrive.com/docs/api/v1/Roles#addOrUpdateRoleSetting)

[PUT\\
\\
Update role details](https://developers.pipedrive.com/docs/api/v1/Roles#updateRole)

[PUT\\
\\
Update pipeline visibility for a role](https://developers.pipedrive.com/docs/api/v1/Roles#updateRolePipelines)

[DELETE\\
\\
Delete a role](https://developers.pipedrive.com/docs/api/v1/Roles#deleteRole)

[DELETE\\
\\
Delete a role assignment](https://developers.pipedrive.com/docs/api/v1/Roles#deleteRoleAssignment)

[Stages](https://developers.pipedrive.com/docs/api/v1/Stages)

[Subscriptions](https://developers.pipedrive.com/docs/api/v1/Subscriptions)

[Tasks](https://developers.pipedrive.com/docs/api/v1/Tasks)

[Users](https://developers.pipedrive.com/docs/api/v1/Users)

[UserConnections](https://developers.pipedrive.com/docs/api/v1/UserConnections)

[UserSettings](https://developers.pipedrive.com/docs/api/v1/UserSettings)

[Webhooks](https://developers.pipedrive.com/docs/api/v1/Webhooks)

## Roles

Run in Postman

Roles are a part of the Visibility groups’ feature that allow the admin user to categorize other users and dictate what items they will be allowed access to see.

#### Get all roles

![Copy link](<Base64-Image-Removed>)

Returns all the roles within the company.

API v1

###### Cost

20

###### Request

GET

/v1/roles

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

#### Get one role

![Copy link](<Base64-Image-Removed>)

Returns the details of a specific role.

API v1

###### Cost

2

###### Request

GET

/v1/roles/{id}

###### Path parameters

id

integer

required

The ID of the role

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

#### List role assignments

![Copy link](<Base64-Image-Removed>)

Returns all users assigned to a role.

API v1

###### Cost

10

###### Request

GET

/v1/roles/{id}/assignments

###### Path parameters

id

integer

required

The ID of the role

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

#### List role settings

![Copy link](<Base64-Image-Removed>)

Returns the visibility settings of a specific role.

API v1

###### Cost

20

###### Request

GET

/v1/roles/{id}/settings

###### Path parameters

id

integer

required

The ID of the role

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }

#### List pipeline visibility for a role

![Copy link](<Base64-Image-Removed>)

Returns the list of either visible or hidden pipeline IDs for a specific role. For more information on pipeline visibility, please refer to the [Visibility groups article](https://support.pipedrive.com/en/article/visibility-groups).

API v1

###### Cost

20

###### Request

GET

/v1/roles/{id}/pipelines

###### Path parameters

id

integer

required

The ID of the role

###### Query parameters

visible

boolean

Whether to return the visible or hidden pipelines for the role

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

#### Add a role

![Copy link](<Base64-Image-Removed>)

Adds a new role.

API v1

###### Cost

10

###### Request

POST

/v1/roles

###### Body parameters

application/json

name

string

required

The name of the role

parent\_role\_id

integer

The ID of the parent role

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }

#### Add role assignment

![Copy link](<Base64-Image-Removed>)

Assigns a user to a role.

API v1

###### Cost

10

###### Request

POST

/v1/roles/{id}/assignments

###### Path parameters

id

integer

required

The ID of the role

###### Body parameters

application/json

user\_id

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

#### Add or update role setting

![Copy link](<Base64-Image-Removed>)

Adds or updates the visibility setting for a role.

API v1

###### Cost

10

###### Request

POST

/v1/roles/{id}/settings

###### Path parameters

id

integer

required

The ID of the role

###### Body parameters

application/json

setting\_key

string

required

Values

deal\_default\_visibility

lead\_default\_visibility

org\_default\_visibility

person\_default\_visibility

product\_default\_visibility

value

integer

required

Possible values for the `default_visibility` setting depending on the subscription plan:

| **Value** | **Description** |
| --- | --- |
| `1` | Owner & Followers |
| `3` | Entire company |

**Essential / Advanced plan**

| **Value** | **Description** |
| --- | --- |
| `1` | Owner only |
| `3` | Owner's visibility group |
| `5` | Owner's visibility group and sub-groups |
| `7` | Entire company |

**Professional / Enterprise plan**

Read more about visibility groups [here](https://support.pipedrive.com/en/article/visibility-groups).

Values

1

3

5

7

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }

#### Update role details

![Copy link](<Base64-Image-Removed>)

Updates the parent role and/or the name of a specific role.

API v1

###### Cost

10

###### Request

PUT

/v1/roles/{id}

###### Path parameters

id

integer

required

The ID of the role

###### Body parameters

application/json

parent\_role\_id

integer

The ID of the parent role

name

string

The name of the role

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }

#### Update pipeline visibility for a role

![Copy link](<Base64-Image-Removed>)

Updates the specified pipelines to be visible and/or hidden for a specific role. For more information on pipeline visibility, please refer to the [Visibility groups article](https://support.pipedrive.com/en/article/visibility-groups).

API v1

###### Cost

10

###### Request

PUT

/v1/roles/{id}/pipelines

###### Path parameters

id

integer

required

The ID of the role

###### Body parameters

application/json

visible\_pipeline\_ids

object

required

The pipeline IDs to make the pipelines visible (add) and/or hidden (remove) for the specified role. It requires the following JSON structure: `{ "add": "[1]", "remove": "[3, 4]" }`.

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }

#### Delete a role

![Copy link](<Base64-Image-Removed>)

Marks a role as deleted.

API v1

###### Cost

6

###### Request

DELETE

/v1/roles/{id}

###### Path parameters

id

integer

required

The ID of the role

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }

#### Delete a role assignment

![Copy link](<Base64-Image-Removed>)

Removes the assigned user from a role and adds to the default role.

API v1

###### Cost

6

###### Request

DELETE

/v1/roles/{id}/assignments

###### Path parameters

id

integer

required

The ID of the role

###### Body parameters

application/json

user\_id

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