from sqlalchemy.orm import Session
from src.infrastructure.models.employee_model import EmpleadoModel
from datetime import datetime


class OracleEmployeeRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, data):

        entity = EmpleadoModel(
            EMP_EMPRESA=data.emp_empresa,
            EMP_CODIGO=data.emp_codigo,
            EMP_ID=data.emp_id,
            EMP_NOMBRE=data.emp_nombre,
            EMP_SEXO=data.emp_sexo,
            EMP_ESTCIVIL=data.emp_estcivil,
            EMP_DIRECCION=data.emp_direccion,
            EMP_DEPARTAMENTO=data.emp_departamento,
            EMP_CARGO=data.emp_cargo,
            EMP_NIVEL=data.emp_nivel,
            EMP_CONTRATO=data.emp_contrato,
            EMP_CENTRO=data.emp_centro,
            EMP_ESTADO=data.emp_estado,
            EMP_MAIL=data.emp_mail,
            EMP_TELEFONO1=data.emp_telefono1,
            EMP_FECHANAC=data.emp_fechanac,
            CREA_FECHA=datetime.now()
        )

        self.db.add(entity)
        self.db.commit()
        self.db.refresh(entity)

        return entity

    def update(self, data):

        entity = (
            self.db.query(EmpleadoModel)
            .filter(
                EmpleadoModel.EMP_EMPRESA == data.emp_empresa,
                EmpleadoModel.EMP_CODIGO == data.emp_codigo
            )
            .first()
        )

        if not entity:
            raise Exception("Empleado no encontrado")

        entity.EMP_NOMBRE = data.emp_nombre
        entity.EMP_SEXO = data.emp_sexo
        entity.EMP_ESTCIVIL = data.emp_estcivil
        entity.EMP_DIRECCION = data.emp_direccion
        entity.EMP_CARGO = data.emp_cargo
        entity.EMP_NIVEL = data.emp_nivel
        entity.EMP_FECHANAC = data.emp_fechanac

        entity.MOD_FECHA = datetime.now()

        self.db.commit()
        self.db.refresh(entity)

        return entity