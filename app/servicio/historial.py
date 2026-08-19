from app.model.historial import  Historial

from sqlalchemy.orm import  Session
from app.schemas.historia_dto import HistoriasDTO

def crear_historia(db:Session, historia:HistoriasDTO):

    historia_db = Historial(
        **historia.model_dump()
    )

    db.add(historia_db)
    db.commit()
    db.refresh(historia_db)
    return historia_db

def obtener_historias_paciente_id(db:Session, id:int)->Historial|None:

    historial = db.query(Historial).filter(Historial.paciente_id==id).first()

    return historial

def obtener_historial_id(db:Session, id:int):
    historial = db.query(Historial).filter(Historial.id == id).first()

    return historial

def actualizar_historias(
    db: Session,
    id: int,
    datos: HistoriasDTO
):
    historial = (
        db.query(Historial)
        .filter(Historial.id == id)
        .first()
    )

    if not historial:
        return None

    cambios = datos.model_dump(exclude_unset=True)

    for campo, valor in cambios.items():
        setattr(historial, campo, valor)

    db.commit()
    db.refresh(historial)

    return historial