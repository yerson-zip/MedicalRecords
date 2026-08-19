from datetime import datetime

from pydantic import BaseModel

class HistoriasDTO(BaseModel):
    paciente_id:int
    medico_id:int
    fecha: datetime
    diagnostico:str
    sintomas:str
    tratamiento:str
    observacion:str

    model_config = {"from_attributes": True}