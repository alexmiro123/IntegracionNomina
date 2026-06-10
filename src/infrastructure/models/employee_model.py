from sqlalchemy import Column, Integer, String, Date, Numeric
from src.infrastructure.database.base import Base


class EmpleadoModel(Base):
    __tablename__ = "EMPLEADO"

    EMP_EMPRESA = Column(Integer, primary_key=True)
    EMP_CODIGO = Column(Integer, primary_key=True)

    EMP_ID = Column(String(10), nullable=False)
    EMP_NOMBRE = Column(String(100), nullable=False)

    EMP_INACTIVO = Column(Integer, default=0)

    EMP_DEPARTAMENTO = Column(Integer, nullable=False)
    EMP_DETALLE = Column(Integer)

    EMP_RUC_CEDULA = Column(String(20))
    EMP_DIRECCION = Column(String(500), nullable=False)

    EMP_CIUDAD = Column(Integer)

    EMP_TELEFONO1 = Column(String(20))
    EMP_TELEFONO2 = Column(String(20))
    EMP_TELEFONO3 = Column(String(20))

    EMP_MAIL = Column(String(100))

    EMP_CONTRATO = Column(Integer, nullable=False)
    EMP_ALMACEN = Column(Integer, nullable=False)

    EMP_SUELDO = Column(Numeric(17, 4))

    EMP_ESTADO = Column(Integer, nullable=False)
    EMP_CARGO = Column(Integer, nullable=False)

    EMP_SEXO = Column(Integer, nullable=False)
    EMP_ESTCIVIL = Column(Integer, nullable=False)

    EMP_TSANGRE = Column(String(20))
    EMP_TITULO = Column(Integer)
    EMP_NIVEL = Column(Integer, nullable=False)

    EMP_NUMCARGAS = Column(Integer)
    EMP_CARGSUBESCOL = Column(Integer)

    EMP_BANNOM = Column(Integer)
    EMP_TCUENTA = Column(Integer)

    EMP_CUENTA = Column(String(20))
    EMP_LIBMILITAR = Column(String(20))
    EMP_CODIESS = Column(String(20))

    EMP_ZONAIESS = Column(Integer, nullable=False)

    EMP_ACTAIESS = Column(String(100))
    EMP_LIBAHORRO = Column(String(20))

    EMP_FECHANAC = Column(Date)
    EMP_FECHAING = Column(Date)
    EMP_FECHARET = Column(Date)

    EMP_ANTICIPO = Column(Numeric(17, 4))

    EMP_CENTRO = Column(Integer, nullable=False)
    EMP_TIPOLIC = Column(String(2))
    EMP_FECHALIC = Column(Date)
    EMP_TIPOCED = Column(String(1))

    EMP_CIUDADDIR = Column(String(10))
    EMP_COMISION = Column(String(1))

    EMP_FECHA_VAC = Column(Date)
    EMP_DIAS = Column(Integer)

    EMP_CALCULO_HORA = Column(Integer)
    EMP_SUELDO1 = Column(Numeric(17, 4))

    EMP_CARPERSONA = Column(Integer)
    EMP_NCONTRATO = Column(String(10))

    EMP_FRESERVA = Column(Integer)
    EMP_NROL = Column(Integer)

    EMP_HORARIO = Column(Integer)

    EMP_MHE = Column(Integer, default=0)
    EMP_MBP = Column(Integer, default=0)

    EMP_USUARIO = Column(Integer)

    EMP_13 = Column(Integer, default=0)
    EMP_14 = Column(Integer, default=0)
    EMP_DISCAPACITADO = Column(Integer, default=0)

    EMP_PTG_DISCAPACIDAD = Column(Numeric(17, 4))

    EMP_SECTOR = Column(String(200))
    EMP_TDISCAPACIDAD = Column(String(200))

    EMP_EXTENSION = Column(Integer)
    EMP_IP = Column(String(20))
    EMP_MAIL_OFI = Column(String(100))

    EMP_CENTRO_PADRE = Column(Integer)
    EMP_REPORTA = Column(Integer)
    EMP_NIVEL_REPORTA = Column(Integer)

    EMP_DEP_NIVEL_BAJO1 = Column(Integer)
    EMP_DEP_NIVEL_BAJO2 = Column(Integer)