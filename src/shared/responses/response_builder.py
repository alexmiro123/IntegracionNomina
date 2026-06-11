from src.shared.responses.api_response import (
    ApiResponse
)

class ResponseBuilder:

    @staticmethod
    def success(
        data=None,
        message="Proceso ejecutado correctamente",
        status=200
    ):
        return ApiResponse(
            Success=True,
            Message=message,
            Status=status,
            Data=data
        )

    @staticmethod
    def error(
        message,
        status=400
    ):
        return ApiResponse(
            Success=False,
            Message=message,
            Status=status
        )