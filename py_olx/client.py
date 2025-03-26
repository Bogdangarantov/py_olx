from .user import UserAPI
from .ads import AdsAPI


class OLXClient:
    def __init__(self, access_token: str):
        """Initialize the client with an access token."""
        self.access_token = access_token
        self.user = UserAPI(access_token=access_token)
        self.ads = AdsAPI(access_token=access_token)
