from datetime import datetime

from sqlalchemy import Integer, func, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Historial(Base):
    __tablename__="historial"

    id:Mapped[int]          = mapped_column(primary_key=True, autoincrement=True)
    paciente_id:Mapped[int] = mapped_column(Integer)
    medico_id:Mapped[int]   = mapped_column(Integer)
    fecha:Mapped[datetime]  = mapped_column(server_default=func.now())
    diagnostico:Mapped[str] = mapped_column(String(255))
    sintomas:Mapped[str]    = mapped_column(String(255))
    tratamiento:Mapped[str] = mapped_column(String(255))
    observacion:Mapped[str] = mapped_column(String(255))
    activo:Mapped[bool]     = mapped_column(Boolean, default=True)


