---
url: "https://developers.pipedrive.com/docs/api/v1/Subscriptions"
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

[GET\\
\\
Get details of a subscription](https://developers.pipedrive.com/docs/api/v1/Subscriptions#getSubscription)

[GET\\
\\
Find subscription by deal](https://developers.pipedrive.com/docs/api/v1/Subscriptions#findSubscriptionByDeal)

[GET\\
\\
Get all payments of a subscription](https://developers.pipedrive.com/docs/api/v1/Subscriptions#getSubscriptionPayments)

[POST\\
\\
Add a recurring subscription](https://developers.pipedrive.com/docs/api/v1/Subscriptions#addRecurringSubscription)

[POST\\
\\
Add an installment subscription](https://developers.pipedrive.com/docs/api/v1/Subscriptions#addSubscriptionInstallment)

[PUT\\
\\
Update a recurring subscription](https://developers.pipedrive.com/docs/api/v1/Subscriptions#updateRecurringSubscription)

[PUT\\
\\
Update an installment subscription](https://developers.pipedrive.com/docs/api/v1/Subscriptions#updateSubscriptionInstallment)

[PUT\\
\\
Cancel a recurring subscription](https://developers.pipedrive.com/docs/api/v1/Subscriptions#cancelRecurringSubscription)

[DELETE\\
\\
Delete a subscription](https://developers.pipedrive.com/docs/api/v1/Subscriptions#deleteSubscription)

[Tasks](https://developers.pipedrive.com/docs/api/v1/Tasks)

[Users](https://developers.pipedrive.com/docs/api/v1/Users)

[UserConnections](https://developers.pipedrive.com/docs/api/v1/UserConnections)

[UserSettings](https://developers.pipedrive.com/docs/api/v1/UserSettings)

[Webhooks](https://developers.pipedrive.com/docs/api/v1/Webhooks)

## Subscriptions

Run in Postman

Subscriptions represent the revenue that is occurring over time with payments of varying amounts and payment dates (installment subscription) or over fixed intervals of time with payments of the same amount (recurring subscription).

#### Get details of a subscription

![Copy link](<Base64-Image-Removed>)

Returns details of an installment or a recurring subscription.

Deprecated endpoint

###### Cost

2

###### Request

GET

/v1/subscriptions/{id}

###### Path parameters

id

integer

required

The ID of the subscription

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }

#### Find subscription by deal

![Copy link](<Base64-Image-Removed>)

Returns details of an installment or a recurring subscription by the deal ID.

Deprecated endpoint

###### Cost

2

###### Request

GET

/v1/subscriptions/find/{dealId}

###### Path parameters

dealId

integer

required

The ID of the deal

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }

#### Get all payments of a subscription

![Copy link](<Base64-Image-Removed>)

Returns all payments of an installment or recurring subscription.

Deprecated endpoint

###### Cost

20

###### Request

GET

/v1/subscriptions/{id}/payments

###### Path parameters

id

integer

required

The ID of the subscription

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":\[ ... \]

#### Add a recurring subscription

![Copy link](<Base64-Image-Removed>)

Adds a new recurring subscription.

Deprecated endpoint

###### Cost

10

###### Request

POST

/v1/subscriptions/recurring

###### Body parameters

application/json

deal\_id

integer

required

The ID of the deal this recurring subscription is associated with

currency

string

required

The currency of the recurring subscription. Accepts a 3-character currency code.

description

string

The description of the recurring subscription

cadence\_type

string

required

The interval between payments

Values

weekly

monthly

quarterly

yearly

cycles\_count

integer

Shows how many payments the subscription has. Note that one field must be set: `cycles_count` or `infinite`. If `cycles_count` is set, then `cycle_amount` and `start_date` are also required.

cycle\_amount

integer

required

The amount of each payment

start\_date

string

required

The start date of the recurring subscription. Format: YYYY-MM-DD

Format

date

infinite

boolean

This indicates that the recurring subscription will last until it's manually canceled or deleted. Note that only one field must be set: `cycles_count` or `infinite`.

payments

array

Array of additional payments. It requires a minimum structure as follows: \[{ amount:SUM, description:DESCRIPTION, due\_at:PAYMENT\_DATE }\]. Replace SUM with a payment amount, DESCRIPTION with an explanation string, PAYMENT\_DATE with a date (format YYYY-MM-DD).

update\_deal\_value

boolean

Indicates that the deal value must be set to recurring subscription's MRR value

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }

#### Add an installment subscription

![Copy link](<Base64-Image-Removed>)

Adds a new installment subscription.

Deprecated endpoint

###### Cost

10

###### Request

POST

/v1/subscriptions/installment

###### Body parameters

application/json

deal\_id

integer

required

The ID of the deal this installment subscription is associated with

currency

string

required

The currency of the installment subscription. Accepts a 3-character currency code.

payments

array

required

Array of payments. It requires a minimum structure as follows: \[{ amount:SUM, description:DESCRIPTION, due\_at:PAYMENT\_DATE }\]. Replace SUM with a payment amount, DESCRIPTION with an explanation string, PAYMENT\_DATE with a date (format YYYY-MM-DD).

update\_deal\_value

boolean

Indicates that the deal value must be set to the installment subscription's total value

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }

#### Update a recurring subscription

![Copy link](<Base64-Image-Removed>)

Updates a recurring subscription.

Deprecated endpoint

###### Cost

10

###### Request

PUT

/v1/subscriptions/recurring/{id}

###### Path parameters

id

integer

required

The ID of the subscription

###### Body parameters

application/json

description

string

The description of the recurring subscription

cycle\_amount

integer

The amount of each payment

payments

array

Array of additional payments. It requires a minimum structure as follows: \[{ amount:SUM, description:DESCRIPTION, due\_at:PAYMENT\_DATE }\]. Replace SUM with a payment amount, DESCRIPTION with an explanation string, PAYMENT\_DATE with a date (format YYYY-MM-DD).

update\_deal\_value

boolean

Indicates that the deal value must be set to recurring subscription's MRR value

effective\_date

string

required

All payments after that date will be affected. Format: YYYY-MM-DD

Format

date

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }

#### Update an installment subscription

![Copy link](<Base64-Image-Removed>)

Updates an installment subscription.

Deprecated endpoint

###### Cost

10

###### Request

PUT

/v1/subscriptions/installment/{id}

###### Path parameters

id

integer

required

The ID of the subscription

###### Body parameters

application/json

payments

array

required

Array of payments. It requires a minimum structure as follows: \[{ amount:SUM, description:DESCRIPTION, due\_at:PAYMENT\_DATE }\]. Replace SUM with a payment amount, DESCRIPTION with a explanation string, PAYMENT\_DATE with a date (format YYYY-MM-DD).

update\_deal\_value

boolean

Indicates that the deal value must be set to installment subscription's total value

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }

#### Cancel a recurring subscription

![Copy link](<Base64-Image-Removed>)

Cancels a recurring subscription.

Deprecated endpoint

###### Cost

10

###### Request

PUT

/v1/subscriptions/recurring/{id}/cancel

###### Path parameters

id

integer

required

The ID of the subscription

###### Body parameters

application/json

end\_date

string

The subscription termination date. All payments after the specified date will be deleted. The end\_date of the subscription will be set to the due date of the payment to follow the specified date. Default value is the current date.

Format

date

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "success":true
- ▶


"data":{ ... }

#### Delete a subscription

![Copy link](<Base64-Image-Removed>)

Marks an installment or a recurring subscription as deleted.

Deprecated endpoint

###### Cost

6

###### Request

DELETE

/v1/subscriptions/{id}

###### Path parameters

id

integer

required

The ID of the subscription

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