import uvicorn
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.schemas.historia_dto import HistoriasDTO
from app.database import get_db, engine
from app.model.historial import Base
from app.servicio.historial import crear_historia, obtener_historias_paciente_id, obtener_historial_id
Base.metadata.create_all(bind=engine)

app= FastAPI()


@app.post("/historial")
def crearHistoria(historia:HistoriasDTO,db:Session=Depends(get_db)):
    return crear_historia(db,historia)

@app.get("/historial")
def obtenerHistorialPorIdPaciente(paciente_id:int, db:Session=Depends(get_db)):
    return obtener_historias_paciente_id(db,paciente_id)

@app.get("/historial/{id}")
def obtenerHistorialPorId(historial_id:int, db:Session=Depends(get_db)):
    return obtener_historias_paciente_id(db,historial_id)

if __name__ == "__main__":
    uvicorn.run(app, port=8000)