from src.infrastructure.models.almacen_model import (AlmacenModel)


CATALOGS = {

    "ALMACEN": (
        AlmacenModel,
        AlmacenModel.ALM_EMPRESA,
        AlmacenModel.ALM_CODIGO
    ),


}