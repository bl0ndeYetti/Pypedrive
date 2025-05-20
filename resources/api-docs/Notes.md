---
url: "https://developers.pipedrive.com/docs/api/v1/Notes"
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

[GET\\
\\
Get all notes](https://developers.pipedrive.com/docs/api/v1/Notes#getNotes)

[GET\\
\\
Get one note](https://developers.pipedrive.com/docs/api/v1/Notes#getNote)

[GET\\
\\
Get all comments for a note](https://developers.pipedrive.com/docs/api/v1/Notes#getNoteComments)

[GET\\
\\
Get one comment](https://developers.pipedrive.com/docs/api/v1/Notes#getComment)

[POST\\
\\
Add a note](https://developers.pipedrive.com/docs/api/v1/Notes#addNote)

[POST\\
\\
Add a comment to a note](https://developers.pipedrive.com/docs/api/v1/Notes#addNoteComment)

[PUT\\
\\
Update a note](https://developers.pipedrive.com/docs/api/v1/Notes#updateNote)

[PUT\\
\\
Update a comment related to a note](https://developers.pipedrive.com/docs/api/v1/Notes#updateCommentForNote)

[DELETE\\
\\
Delete a note](https://developers.pipedrive.com/docs/api/v1/Notes#deleteNote)

[DELETE\\
\\
Delete a comment related to a note](https://developers.pipedrive.com/docs/api/v1/Notes#deleteComment)

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

## Notes

Run in Postman

Notes are pieces of textual (HTML-formatted) information that can be attached to deals, persons and organizations. Notes are usually displayed in the UI in chronological order – newest first – and in context with other updates regarding the item they are attached to. The maximum note size is approximately 100,000 characters (or 100KB per note).

#### Get all notes

![Copy link](<Base64-Image-Removed>)

Returns all notes.

API v1

###### Cost

20

###### Request

GET

/v1/notes

###### Query parameters

user\_id

integer

The ID of the user whose notes to fetch. If omitted, notes by all users will be returned.

lead\_id

string

The ID of the lead which notes to fetch. If omitted, notes about all leads will be returned.

Format

uuid

deal\_id

integer

The ID of the deal which notes to fetch. If omitted, notes about all deals will be returned.

person\_id

integer

The ID of the person whose notes to fetch. If omitted, notes about all persons will be returned.

org\_id

integer

The ID of the organization which notes to fetch. If omitted, notes about all organizations will be returned.

project\_id

integer

The ID of the project which notes to fetch. If omitted, notes about all projects will be returned.

start

integer

Pagination start

Default

0

limit

integer

Items shown per page

sort

string

The field names and sorting mode separated by a comma ( `field_name_1 ASC`, `field_name_2 DESC`). Only first-level field keys are supported (no nested keys). Supported fields: `id`, `user_id`, `deal_id`, `person_id`, `org_id`, `content`, `add_time`, `update_time`.

start\_date

string

The date in format of YYYY-MM-DD from which notes to fetch

Format

date

end\_date

string

The date in format of YYYY-MM-DD until which notes to fetch to

Format

date

pinned\_to\_lead\_flag

number

If set, the results are filtered by note to lead pinning state

Values

0

1

pinned\_to\_deal\_flag

number

If set, the results are filtered by note to deal pinning state

Values

0

1

pinned\_to\_organization\_flag

number

If set, the results are filtered by note to organization pinning state

Values

0

1

pinned\_to\_person\_flag

number

If set, the results are filtered by note to person pinning state

Values

0

1

pinned\_to\_project\_flag

number

If set, the results are filtered by note to project pinning state

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
- ▶


"additional\_data":{ ... }

#### Get one note

![Copy link](<Base64-Image-Removed>)

Returns details about a specific note.

API v1

###### Cost

2

###### Request

GET

/v1/notes/{id}

###### Path parameters

id

integer

required

The ID of the note

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }

#### Get all comments for a note

![Copy link](<Base64-Image-Removed>)

Returns all comments associated with a note.

API v1

###### Cost

20

###### Request

GET

/v1/notes/{id}/comments

###### Path parameters

id

integer

required

The ID of the note

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

#### Get one comment

![Copy link](<Base64-Image-Removed>)

Returns the details of a comment.

API v1

###### Cost

2

###### Request

GET

/v1/notes/{id}/comments/{commentId}

###### Path parameters

id

integer

required

The ID of the note

commentId

string

required

The ID of the comment

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

#### Add a note

![Copy link](<Base64-Image-Removed>)

Adds a new note.

API v1

###### Cost

10

###### Request

POST

/v1/notes

###### Body parameters

application/json

content

string

required

The content of the note in HTML format. Subject to sanitization on the back-end.

lead\_id

string

The ID of the lead the note will be attached to. This property is required unless one of ( `deal_id/person_id/org_id/project_id`) is specified.

Format

uuid

deal\_id

integer

The ID of the deal the note will be attached to. This property is required unless one of ( `lead_id/person_id/org_id/project_id`) is specified.

person\_id

integer

The ID of the person this note will be attached to. This property is required unless one of ( `deal_id/lead_id/org_id/project_id`) is specified.

org\_id

integer

The ID of the organization this note will be attached to. This property is required unless one of ( `deal_id/lead_id/person_id/project_id`) is specified.

project\_id

integer

The ID of the project the note will be attached to. This property is required unless one of ( `deal_id/lead_id/person_id/org_id`) is specified.

user\_id

integer

The ID of the user who will be marked as the author of the note. Only an admin can change the author.

add\_time

string

The optional creation date & time of the note in UTC. Can be set in the past or in the future. Format: YYYY-MM-DD HH:MM:SS

pinned\_to\_lead\_flag

If set, the results are filtered by note to lead pinning state ( `lead_id` is also required)

Values

0

1

pinned\_to\_deal\_flag

If set, the results are filtered by note to deal pinning state ( `deal_id` is also required)

Values

0

1

pinned\_to\_organization\_flag

If set, the results are filtered by note to organization pinning state ( `org_id` is also required)

Values

0

1

pinned\_to\_person\_flag

If set, the results are filtered by note to person pinning state ( `person_id` is also required)

Values

0

1

pinned\_to\_project\_flag

If set, the results are filtered by note to project pinning state ( `project_id` is also required)

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

#### Add a comment to a note

![Copy link](<Base64-Image-Removed>)

Adds a new comment to a note.

API v1

###### Cost

10

###### Request

POST

/v1/notes/{id}/comments

###### Path parameters

id

integer

required

The ID of the note

###### Body parameters

application/json

content

string

required

The content of the comment in HTML format. Subject to sanitization on the back-end.

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }

#### Update a note

![Copy link](<Base64-Image-Removed>)

Updates a note.

API v1

###### Cost

10

###### Request

PUT

/v1/notes/{id}

###### Path parameters

id

integer

required

The ID of the note

###### Body parameters

application/json

content

string

The content of the note in HTML format. Subject to sanitization on the back-end.

lead\_id

string

The ID of the lead the note will be attached to

Format

uuid

deal\_id

integer

The ID of the deal the note will be attached to

person\_id

integer

The ID of the person the note will be attached to

org\_id

integer

The ID of the organization the note will be attached to

project\_id

integer

The ID of the project the note will be attached to

user\_id

integer

The ID of the user who will be marked as the author of the note. Only an admin can change the author.

add\_time

string

The optional creation date & time of the note in UTC. Can be set in the past or in the future. Format: YYYY-MM-DD HH:MM:SS

pinned\_to\_lead\_flag

If set, the results are filtered by note to lead pinning state ( `lead_id` is also required)

Values

0

1

pinned\_to\_deal\_flag

If set, the results are filtered by note to deal pinning state ( `deal_id` is also required)

Values

0

1

pinned\_to\_organization\_flag

If set, the results are filtered by note to organization pinning state ( `org_id` is also required)

Values

0

1

pinned\_to\_person\_flag

If set, the results are filtered by note to person pinning state ( `person_id` is also required)

Values

0

1

pinned\_to\_project\_flag

If set, the results are filtered by note to project pinning state ( `project_id` is also required)

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

#### Update a comment related to a note

![Copy link](<Base64-Image-Removed>)

Updates a comment related to a note.

API v1

###### Cost

10

###### Request

PUT

/v1/notes/{id}/comments/{commentId}

###### Path parameters

id

integer

required

The ID of the note

commentId

string

required

The ID of the comment

Format

uuid

###### Body parameters

application/json

content

string

required

The content of the comment in HTML format. Subject to sanitization on the back-end.

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }

#### Delete a note

![Copy link](<Base64-Image-Removed>)

Deletes a specific note.

API v1

###### Cost

6

###### Request

DELETE

/v1/notes/{id}

###### Path parameters

id

integer

required

The ID of the note

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- "data":true

#### Delete a comment related to a note

![Copy link](<Base64-Image-Removed>)

Deletes a comment.

API v1

###### Cost

6

###### Request

DELETE

/v1/notes/{id}/comments/{commentId}

###### Path parameters

id

integer

required

The ID of the note

commentId

string

required

The ID of the comment

Format

uuid

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- "data":true

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