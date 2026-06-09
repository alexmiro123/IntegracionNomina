from pydantic import BaseModel

class ApiResponse(BaseModel):

    Success: bool
    Message: str
    Status: int
    Data: object | None = None
