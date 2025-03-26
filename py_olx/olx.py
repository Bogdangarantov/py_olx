import requests
from py_olx.exceptions import OLXAPIError

class OLX:
    """
    OLX API Interface.

    This class provides methods to interact with the OLX API by sending GET and POST requests
    to specific endpoints. It is used to communicate with the OLX platform and handle authentication
    using an access token.

    Attributes:
        BASE_URL (str): The base URL for the OLX API.
        headers (dict): The default headers for all API requests.

    Methods:
        __init__(access_token: str): Initializes the OLX API interface with the provided access token.
        _get(endpoint: str, params: dict = None): Sends a GET request to the specified endpoint.
        _post(endpoint: str, data: dict = None): Sends a POST request to the specified endpoint.
        _handle_response(response): Handles API responses, parsing JSON data and raising errors when necessary.
    """

    BASE_URL = "https://www.olx.ua/api"
    BASE_URL_V1 = "https://www.olx.ua/api/v1"
    BASE_URL_V2 = "https://www.olx.ua/api/v2"

    def __init__(self, access_token: str):
        """
        Initializes the OLX API interface with the provided access token.

        Args:
            access_token (str): The access token used for authentication with the OLX API.
        """
        self.access_token = access_token
        self.headers = {
            'Accept': '*/*',
            'Host': 'www.olx.ua',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',
            'X-Platform-Type': 'mobile-html5',
            "Authorization": f"Bearer {self.access_token}"
        }

    def _get(self, endpoint: str, params: dict = None, proxy: dict = ""):
        """
        Sends a GET request to the specified endpoint of the OLX API.

        Args:
            endpoint (str): The endpoint to which the GET request will be made.
            params (dict, optional): Optional dictionary of parameters to include in the GET request.
            proxy (str, optional): Optional proxy URL for the request.

        Returns:
            dict: The JSON response from the OLX API, parsed into a dictionary.

        Raises:
            Exception: If the response status code is not 200, an error is raised with the response details.
        """
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.get(url, params=params, headers=self.headers, proxies=proxy)
        return self._handle_response(response)

    def _getV1(self, endpoint: str, params: dict = None, proxy: dict = ""):
        """
        Sends a GET request to the specified endpoint of the OLX API.

        Args:
            endpoint (str): The endpoint to which the GET request will be made.
            params (dict, optional): Optional dictionary of parameters to include in the GET request.
            proxy (str, optional): Optional proxy URL for the request.

        Returns:
            dict: The JSON response from the OLX API, parsed into a dictionary.

        Raises:
            Exception: If the response status code is not 200, an error is raised with the response details.
        """
        url = f"{self.BASE_URL_V1}/{endpoint}"
        response = requests.get(url, params=params, headers=self.headers, proxies=proxy)
        return self._handle_response(response)

    def _getV2(self, endpoint: str, params: dict = None, proxy: dict = ""):
        """
        Sends a GET request to the specified endpoint of the OLX API.

        Args:
            endpoint (str): The endpoint to which the GET request will be made.
            params (dict, optional): Optional dictionary of parameters to include in the GET request.
            proxy (str, optional): Optional proxy URL for the request.

        Returns:
            dict: The JSON response from the OLX API, parsed into a dictionary.

        Raises:
            Exception: If the response status code is not 200, an error is raised with the response details.
        """
        url = f"{self.BASE_URL_V2}/{endpoint}"
        response = requests.get(url, params=params, headers=self.headers, proxies=proxy)
        return self._handle_response(response)

    def _post(self, endpoint: str, data: dict = None):
        """
        Sends a POST request to the specified endpoint of the OLX API.

        Args:
            endpoint (str): The endpoint to which the POST request will be made.
            data (dict, optional): Optional dictionary of data to include in the POST request as JSON.

        Returns:
            dict: The JSON response from the OLX API, parsed into a dictionary.

        Raises:
            Exception: If the response status code is not 200, an error is raised with the response details.
        """
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.post(url, json=data, headers=self.headers)
        return self._handle_response(response)

    def _handle_response(self, response):
        """
        Handles the API response by checking the status code and raising errors if needed.

        Args:
            response (requests.Response): The response object returned from the request.

        Returns:
            dict: The JSON response parsed into a dictionary if the status code is 200.

        Raises:
            Exception: If the status code is not 200, an error is raised with the status code and message.
        """
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 400:
            raise OLXAPIError(response.status_code,f"The OLX API returned an 400 - {response.json()}")
        else:
            raise Exception(f"OLX API error: {response.status_code} - {response.text}")
