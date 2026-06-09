class BusinessException(Exception):

    def __init__(
        self,
        message: str,
        status_code: int = 400
    ):
        self.message = message
        self.status_code = status_code



class UnauthorizedException(Exception):

    def __init__(self):

        self.message = "No autorizado"
        self.status_code = 401        



class NotFoundException(Exception):

    def __init__(self, message):

        self.message = message
        self.status_code = 404        


class ValidationException(BusinessException):

    def __init__(
            self,
            message: str
    ):
        super().__init__(
            message=message,
            status_code=422
        )        