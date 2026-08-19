

import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.historia_dto import HistoriasDTO
from app.database import get_db, engine
from app.model.historial import Base
from app.servicio.historial import crear_historia, obtener_historias_paciente_id, obtener_historial_id, actualizar_historias
from app.model.historial import Historial

Base.metadata.create_all(bind=engine)

app= FastAPI()


@app.post("/historias")
def crearHistoria(historia:HistoriasDTO,db:Session=Depends(get_db)):
    return crear_historia(db,historia)

@app.get("/historias")
def obtenerHistorialPorIdPaciente(paciente_id:int, db:Session=Depends(get_db)):

    return obtener_historias_paciente_id(db,paciente_id)

@app.get("/historias/{id}")
def obtenerHistorialPorId(historial_id:int, db:Session=Depends(get_db)):

    historia_response: Historial|None =obtener_historial_id(db, historial_id)

    if not historia_response:
        raise HTTPException(status_code=404, detail="Historia no existente")

    return
@app.put("/historias/{id}")
def actualizarHisotria(id:int, historia:HistoriasDTO,db:Session=Depends(get_db)):

    return actualizar_historias(db, id, historia)


if __name__ == "__main__":
    uvicorn.run(app, port=8000)