---
url: "https://developers.pipedrive.com/docs/api/v1/Oauth"
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

[GET\\
\\
Requesting authorization](https://developers.pipedrive.com/docs/api/v1/Oauth#authorize)

[POST\\
\\
Getting the tokens](https://developers.pipedrive.com/docs/api/v1/Oauth#get-tokens)

[POST\\
\\
Refreshing the tokens](https://developers.pipedrive.com/docs/api/v1/Oauth#refresh-tokens)

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

## OAuth 2.0

Run in Postman

Using OAuth 2.0 is necessary for developing apps that are available in the Pipedrive Marketplace. Authorization via OAuth 2.0 is a well-known and stable way to get fine-grained access to an API. To retrieve OAuth2 tokens you should send requests to the `https://oauth.pipedrive.com` domain. After registering the app, you must add the necessary server-side logic to your app to establish the OAuth flow. Please read more about authorization step on the [Pipedrive Developers page](https://pipedrive.readme.io/docs/marketplace-oauth-authorization).

#### Requesting authorization

![Copy link](<Base64-Image-Removed>)

Authorize a user by redirecting them to the Pipedrive OAuth authorization page and request their permissions to act on their behalf. This step is necessary to implement only when you allow app installation outside of the Marketplace.

API v1

###### Request

GET

/oauth/authorize

###### Query parameters

client\_id

string

required

The client ID provided to you by the Pipedrive Marketplace when you register your app

redirect\_uri

string

required

The callback URL you provided when you registered your app. Authorization code will be sent to that URL (if it matches with the value you entered in the registration form) if a user approves the app install. Or, if a customer declines, the corresponding error will also be sent to this URL.

state

string

You may pass any random string as the state parameter and the same string will be returned to your app after a user authorizes access. It may be used to store the user's session ID from your app or distinguish different responses. Using state may increase security; see RFC-6749.

###### Response

200

OK

As a result of the request, the customer will see a page with the confirmation dialog, which will present the details of your app (title, company name, icon) and explain the permission scopes that you have set for the app. Customers should confirm their wish to install the app by clicking "Allow and install" or deny authorization by clicking "Cancel".

#### Getting the tokens

![Copy link](<Base64-Image-Removed>)

After the customer has confirmed the app installation, you will need to exchange the `authorization_code` to a pair of access and refresh tokens. Using an access token, you can access the user's data through the API.

API v1

###### Request

POST

/oauth/token

###### Header parameters

Authorization

string

required

Base 64 encoded string containing the `client_id` and `client_secret` values. The header value should be `Basic <base64(client_id:client_secret)>`.

###### Body parameters

application/x-www-form-urlencoded

grant\_type

string

Since you are trying to exchange an authorization code for a pair of tokens, you must use the value "authorization\_code"

Default

authorization\_code

Values

authorization\_code

refresh\_token

code

string

The authorization code that you received after the user confirmed app installation

redirect\_uri

string

The callback URL you provided when you registered your app

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "access\_token":"v1u:AQIBAHj+LzTNK1yuuuaLqifzhWb9crUNKTpk4FlQ9rjnXqp/6AErhI98syaV25RmpLJLIgOkAAAAfjB8BgkqhkiG9w0BBwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMbGNxa4UccVoXAmLNAgEQgDsiQ7cNdoRBJeFr1i3KW84RYyM1Qtwq1oSBJOl/NFQdVjDI2iQH0LBhS28DbL2KDvoVIihea9Ryt/9rIQ==:RIDnTOIXo8QirT3DMYw0Y0s8xBbxz59f5IMq7T7WhSz313e2MXRHB6g+8OTNCSqVO7QsUhluoAmOfBP1FNkPycy9txn7t2Uoz9y/JDVf4Givv4MMiK/Xq3I7hO4N6FeD+2GqDJDBn24OW6b0SRIr4FEROhGo3BpcPRGehv46NLn1n5LrqXrQwO9qrGD4gIZe40oO2IQgGL9QAPDfqvZ+JhUtcpAipRLp7cCDRfYU8+sdOFJ+hLffqC8isFcV6iPsNrmj"
- "token\_type":"Bearer"
- "expires\_in":3599
- "refresh\_token":"1:1:2a5496a8bdd0f829dcb09dc8ba82b188f0ea4481"
- "scope":"base"
- "api\_domain":"https://user-company.pipedrive.com"

#### Refreshing the tokens

![Copy link](<Base64-Image-Removed>)

The `access_token` has a lifetime. After a period of time, which was returned to you in `expires_in` JSON property, the `access_token` will be invalid, and you can no longer use it to get data from our API. To refresh the `access_token`, you must use the `refresh_token`.

API v1

###### Request

POST

/oauth/token

###### Header parameters

Authorization

string

required

Base 64 encoded string containing the `client_id` and `client_secret` values. The header value should be `Basic <base64(client_id:client_secret)>`.

###### Body parameters

application/x-www-form-urlencoded

grant\_type

string

Since you are to refresh your access\_token, you must use the value "refresh\_token"

Default

refresh\_token

Values

authorization\_code

refresh\_token

refresh\_token

string

The refresh token that you received after you exchanged the authorization code

###### Response

200

OK

![](<Base64-Image-Removed>)Expand all

![](<Base64-Image-Removed>)Copy code

- "access\_token":"v1u:AQIBAHj+LzTNK1yuuuaLqifzhWb9crUNKTpk4FlQ9rjnXqp/6AErhI98syaV25RmpLJLIgOkAAAAfjB8BgkqhkiG9w0BBwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMbGNxa4UccVoXAmLNAgEQgDsiQ7cNdoRBJeFr1i3KW84RYyM1Qtwq1oSBJOl/NFQdVjDI2iQH0LBhS28DbL2KDvoVIihea9Ryt/9rIQ==:RIDnTOIXo8QirT3DMYw0Y0s8xBbxz59f5IMq7T7WhSz313e2MXRHB6g+8OTNCSqVO7QsUhluoAmOfBP1FNkPycy9txn7t2Uoz9y/JDVf4Givv4MMiK/Xq3I7hO4N6FeD+2GqDJDBn24OW6b0SRIr4FEROhGo3BpcPRGehv46NLn1n5LrqXrQwO9qrGD4gIZe40oO2IQgGL9QAPDfqvZ+JhUtcpAipRLp7cCDRfYU8+sdOFJ+hLffqC8isFcV6iPsNrmj"
- "token\_type":"Bearer"
- "expires\_in":3599
- "refresh\_token":"1:1:2a5496a8bdd0f829dcb09dc8ba82b188f0ea4481"
- "scope":"base"
- "api\_domain":"https://user-company.pipedrive.com"

### Subscribe to Pipedrive’s Developer Newsletter

Your email address

Subscribe

We promise not to send you any marketing materials or spam, just developer news.

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