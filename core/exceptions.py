class APIError(Exception):
    pass


class NotFoundError(APIError):
    pass


class UnauthorizedError(APIError):
    pass


class ServerError(APIError):
    pass