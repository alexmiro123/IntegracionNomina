from src.shared.exceptions.custom_exceptions import BusinessException


class EmployeeRules:

    @staticmethod
    def validate(data):

        if data.emp_sexo not in [1, 2]:
            raise BusinessException("EMP_SEXO debe ser 1(Masculino) o 2(Femenino)", 400)

        if data.emp_estcivil not in [1, 2, 3, 4]:
            raise BusinessException("Estado civil inválido", 400)

        if data.emp_empresa <= 0:
            raise BusinessException("Empresa inválida", 400)

        if not data.emp_nombre.strip():
            raise BusinessException("Nombre requerido", 400)