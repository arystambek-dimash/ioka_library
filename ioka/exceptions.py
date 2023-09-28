class ServiceError(Exception):
    """
    If response code not in (200, 201).
    """


class Unauthorized(Exception):
    """
    Exception raised for unauthorized access errors.

    Attributes:
        message -- explanation of the error
    """


class RequestError(Exception):
    """
    Some required param is missing.
    """

    def __init__(self, param):
        self.param = param

    def __str__(self):
        return "Required parameter '%s' is missing." % self.param
