from src.shared.exceptions.custom_exceptions import BusinessException

class EmployeeRules:

    @staticmethod
    def validate(data, catalog_repository):

        if not catalog_repository.exists_catalog(
            "ALMACEN",
            data.emp_empresa,
            data.emp_almacen
        ):
            raise BusinessException(
                f"EMP_ALMACEN no existe",
                400
            )
        
        if data.emp_sexo not in [1, 2]:
            raise BusinessException("EMP_SEXO debe ser 1(Masculino) o 2(Femenino)", 400)
        
        
        if not data.emp_nombre.strip():
            raise BusinessException("Nombre requerido", 400)