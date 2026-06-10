from pydantic import BaseModel
from datetime import date
from typing import Optional


class EmployeeRequest(BaseModel):

    emp_empresa: int
    emp_codigo: int
    emp_id: str
    emp_nombre: str

    emp_sexo: int  # 1 o 2

    emp_estcivil: int
    emp_direccion: str

    emp_departamento: int
    emp_cargo: int
    emp_nivel: int

    emp_contrato: int
    emp_centro: int
    emp_estado: int

    emp_mail: Optional[str] = None
    emp_telefono1: Optional[str] = None

    emp_fechanac: Optional[date] = None