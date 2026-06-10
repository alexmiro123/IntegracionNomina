from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.infrastructure.database.dependencies import get_db
from src.application.dtos.employee.employee_request import EmployeeRequest

from src.infrastructure.security.jwt_bearer import JWTBearer

from src.infrastructure.persistence.repositories.oracle_employee_repository import (
    OracleEmployeeRepository
)

from src.application.use_cases.employee.save_employee_use_case import (
    SaveEmployeeUseCase
)

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)



# =========================
# CREATE EMPLOYEE
# =========================
@router.post("/create")
async def create_employee(
    request: EmployeeRequest,
    payload=Depends(
        JWTBearer(required_scopes=["employees:create"])
    ),
    db: Session = Depends(get_db)
):

    repository = OracleEmployeeRepository(db)

    use_case = SaveEmployeeUseCase(repository)

    result = use_case.execute(
        request,
        is_update=False
    )

    return {
        "success": True,
        "message": "Empleado creado correctamente",
        "data": result
    }


# =========================
# UPDATE EMPLOYEE
# =========================
@router.put("/update")
async def update_employee(
    request: EmployeeRequest,
    payload=Depends(
        JWTBearer(required_scopes=["employees:update"])
    ),
    db: Session = Depends(get_db)
):

    repository = OracleEmployeeRepository(db)

    use_case = SaveEmployeeUseCase(repository)

    result = use_case.execute(
        request,
        is_update=True
    )

    return {
        "success": True,
        "message": "Empleado actualizado correctamente",
        "data": result
    }