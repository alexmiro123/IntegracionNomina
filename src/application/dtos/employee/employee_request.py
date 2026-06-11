from pydantic import BaseModel
from datetime import date
from typing import Optional


class EmployeeRequest(BaseModel):

    emp_empresa: int
    emp_nombre: str
    emp_departamento: int
    emp_detalle: Optional[str] = None
    emp_ruc_cedula: str
    emp_direccion: str
    emp_ciudad: int
    emp_telefono1: str
    emp_telefono2: Optional[str] = None
    emp_telefono3: Optional[str] = None
    emp_mail: str
    emp_contrato: int
    emp_almacen: int
    emp_sueldo: int
    emp_estado: int
    emp_cargo: int
    emp_sexo: int  
    emp_estcivil: int
    emp_tsangre: str
    emp_titulo: int
    emp_nivel: int
    emp_numcargas: int
    emp_cargsubescol: int | None = None
    emp_bannom: int | None = None
    emp_tcuenta: int | None = None
    emp_cuenta: str | None = None
    emp_libmilitar: str | None = None
    emp_codiess: str
    emp_zonaiess: int
    emp_actaiess: str | None = None
    emp_libahorro: str | None = None
    emp_fechanac: date
    emp_fechaing: date    
    emp_centro: int
    emp_tipolic: str | None = None
    emp_fechalic: Optional[date] = None
    emp_tipoced: Optional[str] = 0
    emp_ciudaddir: Optional[str] = None
    emp_comision: Optional[str] = None
    emp_sueldo1: Optional[int] = 0
    emp_freserva: Optional[int] = 0
    emp_horario: int
    emp_usuario: Optional[int] = None
    emp_mhe: int
    emp_discapacitado: Optional[int] = 0
    emp_ptg_discapacidad: Optional[int] = None
    emp_sector: str
    emp_tdiscapacidad: Optional[str] = None
    emp_centro_padre: Optional[int] = None
    emp_nivel_reporta: int
