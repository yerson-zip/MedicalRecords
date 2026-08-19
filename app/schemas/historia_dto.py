from datetime import datetime

from pydantic import BaseModel

class HistoriasDTO(BaseModel):
    paciente_id:int | None = None
    medico_id:int| None = None
    fecha: datetime| None = None
    diagnostico:str| None = None
    sintomas:str| None = None
    tratamiento:str| None = None
    observacion:str| None = None

    model_config = {"from_attributes": True}