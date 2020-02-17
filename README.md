# gmail-api-example

## Description

An example project to show how gmail inbox access via the gmail API can work.

The general method is a service account granted domain-wide delegation for the
Gmail API (via Gsuite admin), which impersonates a gmail user to access the
mailbox. This avoids the requirement for user interaction in an OAuth
authorization flow.

The manual steps to set this up are described here, and a sample Python script
included in the repo.

References:

https://developers.google.com/identity/protocols/OAuth2ServiceAccount#formingclaimset
https://developers.google.com/gmail/api/auth/scopes
http://googleapis.github.io/google-api-python-client/docs/dyn/gmail_v1.users.messages.html#get

## Manual steps

1. This only works in a GSuite subscription. This is a paid service, you must
   be able to access admin.google.com which has been setup for a domain you own.

2. Go to `console.developers.google.com` and enable the Gmail API, then setup
   the OAuth consent screen (internal scope, minimal config is fine).

3. Create a service account in `console.cloud.google.com` and download a
   private key JSON. No roles are needed. Copy the Unique ID.

4. In the GSuite admin console `admin.google.com`, from the dashboard go to
   Security `->` Advanced Settings `->` Manage API Client Access. Add the
   Unique ID from earlier with a scope of `https://mail.google.com` or some of
   the lower privilege scopes from the Gmail API docs.

5. Run `script.py` with the private key JSON path set correctly.
