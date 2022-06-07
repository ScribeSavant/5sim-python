

class NoPhoneNumberError(Exception):
    """
    Raised when a phone number is not provided.
    """
    pass


class ApiKeyInvalidError(Exception):
    """
    Raised when an invalid API key is provided.
    """
    pass


class BadRequests(Exception):
    """
    Raised when multiple errors are raised.
    """
    pass

class LowBalanceError(Exception):
    """
    Raised when the balance is too low.
    """
    pass
