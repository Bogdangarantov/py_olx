import asyncio

from py_olx import OLXClient
from py_olx import OLXAuth


async def main():
    client = OLXClient("YOUR_ACCESS_TOKEN")
    adv_id = 1234
    adv_info = await client.ads.get_ad(adv_id)
    print(adv_info)
    contact_phone = await client.ads.get_contact_number(ad_id=adv_id)
    print(contact_phone)


async def refresh_token():
    client_id: str = "YOUR CLIENT ID"
    client_secret: str = "YOUR_CLIENT_SECRET"
    refresh_token = "<YOUR_REFRESH_TOKEN>"
    auth = OLXAuth(client_id=client_id, client_secret=client_secret,refresh_token=refresh_token)
    new_tokens = auth.refresh_access_token()
    print("Access Token:", new_tokens.get("access_token"))
    print("Refresh Token:", new_tokens.get("refresh_token"))




# asyncio.run(main())
