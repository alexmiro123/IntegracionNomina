from src.domain.employees.rules.employee_rules import EmployeeRules


class SaveEmployeeUseCase:

    def __init__(self, repository):
        self.repository = repository

    def execute(self, data, is_update: bool):

        # 1. VALIDACIONES
        EmployeeRules.validate(data)

        # 2. DECISIÓN
        if is_update:
            return self.repository.update(data)

        return self.repository.create(data)