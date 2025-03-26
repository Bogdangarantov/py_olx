from .olx import OLX


class UserAPI(OLX):
    """
    Class for interacting with OLX user-related endpoints.

    This class provides methods to retrieve information about the authenticated user,
    access user details by ID, check the account balance, and retrieve available payment methods.
    """

    async def get_authenticated_user(self):
        """
        Retrieve information about the currently authenticated user.

        This method returns the details of the user who is authenticated with the provided access token.

        Returns:
            dict:{
                    "id": 123,
                    "email": "john@mail.com",
                    "status": "confirmed",
                    "name": "John",
                    "phone": 123123123,
                    "phone_login": 123123123,
                    "created_at": "2018-01-29 14:04:13",
                    "last_login_at": "2018-01-30 08:20:28",
                    "avatar": null,
                    "is_business": true
                    }
        Raises:
            HTTPError: If the authentication token is invalid, expired, or the user is not authenticated.
        """
        return self._getV1("users/me")

    async def get_user(self, user_id: int):
        """
        Retrieve user information by user ID.

        This method allows retrieving details of a user based on their unique ID.

        Args:
            user_id (int): The unique identifier of the user whose information is to be fetched.

        Returns:
            dict: {
                    "id": 1,
                    "name": "John",
                    "avatar": null
                    }

        Raises:
            HTTPError: If the request fails due to an invalid user ID, authentication issues, or a network error.
        """
        return self._getV1(f"users/{user_id}")

