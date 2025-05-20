---
url: "https://developers.pipedrive.com/docs/api/v1/Files"
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

[GET\\
\\
Get all files](https://developers.pipedrive.com/docs/api/v1/Files#getFiles)

[GET\\
\\
Get one file](https://developers.pipedrive.com/docs/api/v1/Files#getFile)

[GET\\
\\
Download one file](https://developers.pipedrive.com/docs/api/v1/Files#downloadFile)

[POST\\
\\
Add file](https://developers.pipedrive.com/docs/api/v1/Files#addFile)

[POST\\
\\
Create a remote file and link it to an item](https://developers.pipedrive.com/docs/api/v1/Files#addFileAndLinkIt)

[POST\\
\\
Link a remote file to an item](https://developers.pipedrive.com/docs/api/v1/Files#linkFileToItem)

[PUT\\
\\
Update file details](https://developers.pipedrive.com/docs/api/v1/Files#updateFile)

[DELETE\\
\\
Delete a file](https://developers.pipedrive.com/docs/api/v1/Files#deleteFile)

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

## Files

Run in Postman

Files are documents of any kind (images, spreadsheets, text files, etc.) that are uploaded to Pipedrive, and usually associated with a particular deal, person, organization, product, note or activity. Remote files can only be associated with a particular deal, person or organization. Note that the API currently does not support downloading files although it lets you retrieve a file’s meta-info along with a URL which can be used to download the file by using a standard HTTP GET request.

#### Get all files

![Copy link](<Base64-Image-Removed>)

Returns data about all files.

API v1

###### Cost

20

###### Request

GET

/v1/files

###### Query parameters

start

integer

Pagination start

Default

0

limit

integer

Items shown per page. Please note that a maximum value of 100 is allowed.

sort

string

Supported fields: `id`, `update_time`

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

#### Get one file

![Copy link](<Base64-Image-Removed>)

Returns data about a specific file.

API v1

###### Cost

2

###### Request

GET

/v1/files/{id}

###### Path parameters

id

integer

required

The ID of the file

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }

#### Download one file

![Copy link](<Base64-Image-Removed>)

Initializes a file download.

API v1

###### Cost

20

###### Request

GET

/v1/files/{id}/download

###### Path parameters

id

integer

required

The ID of the file

###### Response

200

OK

#### Add file

![Copy link](<Base64-Image-Removed>)

Lets you upload a file and associate it with a deal, person, organization, activity, product or lead. For more information, see the tutorial for [adding a file](https://pipedrive.readme.io/docs/adding-a-file).

API v1

###### Cost

10

###### Request

POST

/v1/files

###### Body parameters

multipart/form-data

file

string

required

A single file, supplied in the multipart/form-data encoding and contained within the given boundaries

Format

binary

deal\_id

integer

The ID of the deal to associate file(s) with

person\_id

integer

The ID of the person to associate file(s) with

org\_id

integer

The ID of the organization to associate file(s) with

product\_id

integer

The ID of the product to associate file(s) with

activity\_id

integer

The ID of the activity to associate file(s) with

lead\_id

string

The ID of the lead to associate file(s) with

Format

uuid

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }

#### Create a remote file and link it to an item

![Copy link](<Base64-Image-Removed>)

Creates a new empty file in the remote location ( `googledrive`) that will be linked to the item you supply. For more information, see the tutorial for [adding a remote file](https://pipedrive.readme.io/docs/adding-a-remote-file).

API v1

###### Cost

10

###### Request

POST

/v1/files/remote

###### Body parameters

application/x-www-form-urlencoded

file\_type

string

required

The file type

Values

gdoc

gslides

gsheet

gform

gdraw

title

string

required

The title of the file

item\_type

string

required

The item type

Values

deal

organization

person

item\_id

integer

required

The ID of the item to associate the file with

remote\_location

string

required

The location type to send the file to. Only `googledrive` is supported at the moment.

Values

googledrive

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }

#### Link a remote file to an item

![Copy link](<Base64-Image-Removed>)

Links an existing remote file ( `googledrive`) to the item you supply. For more information, see the tutorial for [adding a remote file](https://pipedrive.readme.io/docs/adding-a-remote-file).

API v1

###### Cost

10

###### Request

POST

/v1/files/remoteLink

###### Body parameters

application/x-www-form-urlencoded

item\_type

string

required

The item type

Values

deal

organization

person

item\_id

integer

required

The ID of the item to associate the file with

remote\_id

string

required

The remote item ID

remote\_location

string

required

The location type to send the file to. Only `googledrive` is supported at the moment.

Values

googledrive

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }

#### Update file details

![Copy link](<Base64-Image-Removed>)

Updates the properties of a file.

API v1

###### Cost

10

###### Request

PUT

/v1/files/{id}

###### Path parameters

id

integer

required

The ID of the file

###### Body parameters

application/x-www-form-urlencoded

name

string

The visible name of the file

description

string

The description of the file

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }

#### Delete a file

![Copy link](<Base64-Image-Removed>)

Marks a file as deleted. After 30 days, the file will be permanently deleted.

API v1

###### Cost

6

###### Request

DELETE

/v1/files/{id}

###### Path parameters

id

integer

required

The ID of the file

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