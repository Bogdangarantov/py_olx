import requests


class OLXAuth:
    """
    Class to handle authentication and token refresh for OLX API.

    This class provides functionality to refresh the access token using a refresh token.
    """

    BASE_URL = "https://www.olx.ua/api"

    def __init__(self, client_id: str, client_secret: str, refresh_token: str):
        """
        Initialize the OLXAuth object.

        Args:
            client_id (str): The client ID from the OLX application.
            client_secret (str): The client secret from the OLX application.
            refresh_token (str): The refresh token obtained during the initial authentication process.
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.refresh_token = refresh_token

    def refresh_access_token(self):
        """
        Refresh the OLX access token using the refresh token.

        Returns:
            dict: {
                access_token: string,
                refresh_token: string
            }

        Raises:
            HTTPError: If the request fails to refresh the token or invalid credentials are provided.
        """
        url = f"{self.BASE_URL}/open/auth/refresh_token"
        data = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "refresh_token": self.refresh_token,
            "grant_type": "refresh_token"
        }

        response = requests.post(url, data=data)

        # Handle the response
        if response.status_code == 200:
            return response.json()  # Return the new token details
        else:
            raise Exception(f"Failed to refresh access token: {response.status_code} - {response.text}")

