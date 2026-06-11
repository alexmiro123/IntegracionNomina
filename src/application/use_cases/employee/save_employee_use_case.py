from src.domain.employees.rules.employee_rules import EmployeeRules
from src.domain.employees.rules.employee_rules import (EmployeeRules)
from src.application.dtos.employee.employee_response_create import EmployeeCreatedResponse

class SaveEmployeeUseCase:

    def __init__(
        self,
        employee_repository,
        catalog_repository,
        db
    ):
        self.employee_repository = employee_repository
        self.catalog_repository = catalog_repository
        self.db = db

    def execute(
        self,
        data,
        is_update: bool
    ):

        with self.db.begin():

            EmployeeRules.validate(
                data,
                self.catalog_repository
            )

            if not is_update:

                emp_id, codigo = (
                    self.employee_repository
                    .generate_employee_code(
                        data.emp_empresa,
                        data.emp_almacen
                    )
                )

                employee = (
                    self.employee_repository
                    .create(
                        data,
                        codigo,
                        emp_id
                    )
                )



            else:

                employee = (
                    self.employee_repository
                    .update(data)
                )

            return EmployeeCreatedResponse(
                emp_codigo=employee.EMP_CODIGO,
                emp_id=employee.EMP_ID
            )