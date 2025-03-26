# OLX Python Client (py-olx)

`py-olx` is a Python client library for interacting with the OLX API. It provides an easy way to interact with the OLX platform, allowing you to manage users, ads, and more.

## Features

- Retrieve user information
- Get ad details
- Get contact numbers for ads
- Token management (refresh)

## Installation

You can install the library via pip:

```bash
pip install py-olx
``` 
## 1. Initialize the OLX Client
You need an OLX API access token to authenticate. Once you have the token, initialize the OLX class.
```python
from py_olx import OLX

# Replace with your actual access token
access_token = "your_access_token"
olx = OLX(access_token)
```
## 2.Retrieve Authenticated User
You can retrieve the details of the currently authenticated user.
```python
# Fetch authenticated user details
user_details = olx.user.get_authenticated_user()
print(user_details)
```
## 3. Retrieve User by ID
To retrieve information about a user by their user ID:
```python
user_id = 12345  # Replace with the user ID
user_info = olx.user.get_user(user_id)
print(user_info)
```

## 4.Working with Ads
Get Advertisement by ID
To retrieve details about a specific ad by its ID:

```python
ad_id = 123456  # Replace with the ad ID
ad_details = olx.ads.get_ad(ad_id)
print(ad_details)
```

## 5.Get Contact Number for an Advertisement
To retrieve the contact number for a specific advertisement:

```python
contact_number = olx.ads.get_contact_number(ad_id)
print(contact_number)
```

## 6.Refreshing Token
You can refresh the token using the OLXAuth class. Here is an example of refreshing the token:

```python
from py_olx import OLXAuth

# Replace with the client ID, client secret, and the refresh token you got during initial auth
client_id = "your_client_id"
client_secret = "your_client_secret"
refresh_token = "your_refresh_token"

auth = OLXAuth(client_id, client_secret,refresh_token)
new_access_token = auth.refresh_token()
print(f"New Access Token: {new_access_token}")
```

# Future Features

- [ ] **Posting, Editing, and Deleting Ads**: Implement functionality to post, edit, and delete ads.
- [ ] **Search Ads by Category**: Add search functionality based on categories and filters.
- [ ] **Retrieve and Clear Statistics**: Fetch and reset ad statistics.
- [ ] **Respond to Messages**: Add support for responding to messages related to ads.



