from sqlalchemy.orm import Session
from src.infrastructure.models.employee_model import EmpleadoModel
from datetime import datetime
from sqlalchemy import text

class OracleEmployeeRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, data, codigo, emp_id):

        entity = EmpleadoModel(
            EMP_EMPRESA=data.emp_empresa,
            EMP_CODIGO=codigo,
            EMP_ID=emp_id,
            EMP_NOMBRE=data.emp_nombre,
            EMP_DEPARTAMENTO=data.emp_departamento,
            EMP_DETALLE=data.emp_detalle,
            EMP_RUC_CEDULA=data.emp_ruc_cedula,
            EMP_DIRECCION=data.emp_direccion,
            EMP_CIUDAD=data.emp_ciudad,
            EMP_TELEFONO1=data.emp_telefono1,
            EMP_TELEFONO2=data.emp_telefono2,
            EMP_TELEFONO3=data.emp_telefono3,
            EMP_MAIL=data.emp_mail,
            EMP_CONTRATO=data.emp_contrato,
            EMP_ALMACEN=data.emp_almacen,
            EMP_SUELDO=data.emp_sueldo,
            EMP_ESTADO=data.emp_estado,
            EMP_CARGO=data.emp_cargo,
            EMP_SEXO=data.emp_sexo,
            EMP_ESTCIVIL=data.emp_estcivil,
            EMP_TSANGRE=data.emp_tsangre,
            EMP_TITULO=data.emp_titulo,
            EMP_NIVEL=data.emp_nivel,
            EMP_NUMCARGAS=data.emp_numcargas,
            EMP_CARGSUBESCOL=data.emp_cargsubescol,
            EMP_BANNOM=data.emp_bannom,
            EMP_TCUENTA=data.emp_tcuenta,
            EMP_CUENTA=data.emp_cuenta,
            EMP_LIBMILITAR=data.emp_libmilitar,
            EMP_CODIESS=data.emp_codiess,
            EMP_ZONAIESS=data.emp_zonaiess,
            EMP_ACTAIESS=data.emp_actaiess,
            EMP_LIBAHORRO=data.emp_libahorro,
            EMP_FECHANAC=data.emp_fechanac,
            EMP_FECHAING=data.emp_fechaing,
            EMP_CENTRO=data.emp_centro,
            EMP_TIPOLIC=data.emp_tipolic,
            EMP_FECHALIC=data.emp_fechalic,
            EMP_TIPOCED=data.emp_tipoced,
            EMP_CIUDADDIR=data.emp_ciudaddir,
            EMP_COMISION=data.emp_comision,
            EMP_SUELDO1=data.emp_sueldo1,
            EMP_FRESERVA=data.emp_freserva,
            EMP_HORARIO=data.emp_horario,
            EMP_USUARIO=data.emp_usuario,
            EMP_MHE=data.emp_mhe,
            EMP_DISCAPACITADO=data.emp_discapacitado,
            EMP_PTG_DISCAPACIDAD=data.emp_ptg_discapacidad,
            EMP_SECTOR=data.emp_sector,
            EMP_TDISCAPACIDAD=data.emp_tdiscapacidad,
            EMP_CENTRO_PADRE=data.emp_centro_padre,
            EMP_NIVEL_REPORTA=data.emp_nivel_reporta,
        )

        self.db.add(entity)

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

        return entity
    

    def generate_employee_code(
        self,
        empresa: int,
        almacen: int
    ):

        codigo = self.db.execute(
            text(
                "SELECT empleado_s_codigo.NEXTVAL FROM dual"
            )
        ).scalar()

        if almacen > 0:
            codigo += almacen * (10 ** 7)

        max_id = self.db.execute(
            text("""
                SELECT NVL(MAX(TO_NUMBER(emp_id)),0) + 1
                FROM empleado
                WHERE emp_empresa = :empresa
            """),
            {
                "empresa": empresa
            }
        ).scalar()

        return {
            codigo,
            str(max_id)
        }    