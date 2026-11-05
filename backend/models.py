from sqlmodel import Field, SQLModel, Relationship


class Videos(SQLModel, table=True): 
    id : int | None = Field(default=None, primary_key=True) 
    titulo: str 
    source: str
    categoria: str
    publico: bool
    comentarios: list["Comments"] = Relationship(
        back_populates="video",
        cascade_delete=True
    )

class VideosCreate(SQLModel): 
    titulo: str
    source: str
    categoria: str
    publico: bool

class Comments(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    autor: str
    texto: str
    video_id: int = Field(foreign_key="videos.id", ondelete="CASCADE")
    video: Videos | None = Relationship(back_populates="comentarios")

class CommentsCreate(SQLModel):
    autor: str
    texto: str