class ServiceError(Exception):
    """
    If response code not in (200, 201).
    """