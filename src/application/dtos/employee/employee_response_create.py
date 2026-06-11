from pydantic import BaseModel

class EmployeeCreatedResponse(BaseModel):
    emp_codigo: int
    emp_id: str