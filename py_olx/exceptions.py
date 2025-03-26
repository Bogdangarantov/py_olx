class OLXAPIError(Exception):
    """Кастомна помилка для OLX API."""
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message
        super().__init__(f"OLX API error {status_code}: {message}")