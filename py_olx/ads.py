from .olx import OLX


class AdsAPI(OLX):
    """
    Class for interacting with OLX advertisement-related endpoints.

    This class provides methods to retrieve advertisement details and get contact numbers
    associated with advertisements.
    """

    async def get_ad(self, ad_id: int, proxy: dict = None):
        """
        Retrieve the details of an advertisement by its ID.

        Args:
            :param ad_id:
            :param proxy:
            ad_id (int): The unique identifier of the advertisement.

        Returns:
            dict: A dictionary containing the advertisement details, such as title, description,
                  category, price, and other relevant information.

        Raises:
            HTTPError: If the request fails due to an invalid advertisement ID, authentication issues,
                       or a network error.

        """
        return self._getV1(f"ads/{ad_id}", proxy=proxy)

    async def get_contact_number(self, ad_id: int, proxy: dict = None):
        """
        Retrieve the contact number associated with an advertisement.

        Args:
            :ad_id (int): The unique identifier of the advertisement.

        Returns:
            dict: A dictionary containing the contact information, such as phone numbers related to the advertisement.

        Raises:
            HTTPError: If the request fails due to an invalid advertisement ID, authentication issues,
                       or a network error.
        """
        return self._getV1(f"offers/{ad_id}/limited-phones/", proxy=proxy)
