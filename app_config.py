import os

# Application (client) ID of app registration
CLIENT_ID = "a93ca8d2-2faa-4a0b-afff-8758d7fc85fd"

# Placeholder - for use ONLY during testing.
CLIENT_SECRET = "cOr8Q~ptsnRjtcUiGudKc9R.DYSWhf_jfMaqvbx7"
# In a production app, we recommend you use a more secure method of storing your secret,
# like Azure Key Vault. Or, use an environment variable as described in Flask's documentation:
# https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
# CLIENT_SECRET = os.getenv("CLIENT_SECRET")
# if not CLIENT_SECRET:
#     raise ValueError("Need to define CLIENT_SECRET environment variable")

AUTHORITY = "https://login.microsoftonline.com/consumers"  # For multi-tenant app
# AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

# Used for forming an absolute URL to your redirect URI.
REDIRECT_PATH = "/getAToken45"
# The absolute URL must match the redirect URI you set
# in the app's registration in the Azure portal.

# You can find more Microsoft Graph API endpoints from Graph Explorer
# https://developer.microsoft.com/en-us/graph/graph-explorer
# This resource requires no admin consent
ENDPOINT = 'https://graph.microsoft.com/v1.0/users'

# You can find the proper permission names from this document
# https://docs.microsoft.com/en-us/graph/permissions-reference
SCOPE = ["User.ReadBasic.All"]

# Specifies the token cache should be stored in server-side session
SESSION_TYPE = "filesystem"
