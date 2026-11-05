from requests import session
from sqlmodel import func, select
from fastapi import APIRouter, HTTPException, status

from db import SessionDep
from models import Comments, Videos, VideosCreate, CommentsCreate

router = APIRouter(prefix="/videos", tags=["videos"])


@router.get("/")
def get_videos(session: SessionDep):
    return session.exec(select(Videos)).all()

@router.get("/{video_id}")
def get_video_id(video_id: int, session: SessionDep):
    video_db = session.get(Videos, video_id)
    if not video_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Video no encontrado"
        )
    return video_db

@router.post("/")
def create_video(video_data:VideosCreate, session: SessionDep):
    video = Videos.model_validate(video_data.model_dump()) 
    session.add(video)
    session.commit() 
    session.refresh(video) 
    return video

@router.delete("/{video_id}")
def delete_video(video_id: int, session: SessionDep):
    video = session.get(Videos, video_id)
    if not video:
        raise HTTPException(status_code=404, detail="Video no encontrado")
    session.delete(video)
    session.commit()
    return {"ok": True}


@router.get("/{video_id}/recomendados")
def get_recomendados(video_id: int, session: SessionDep):
    video_db = session.get(Videos, video_id)
    if not video_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Video no encontrado"
        )
    query = (
        select(Videos)
        .where(Videos.categoria == video_db.categoria)
        .where(Videos.id != video_id)
        .order_by(func.random())
        .limit(10)
    )
    return session.exec(query).all()

@router.get("/{video_id}/comentarios")
def get_comentarios(video_id: int, session: SessionDep):
    video_db = session.get(Videos, video_id)
    if not video_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Video no encontrado"
        )
    return video_db.comentarios


@router.post("/{video_id}/comentarios", status_code=status.HTTP_201_CREATED)
def create_comentario(video_id: int, data: CommentsCreate, session: SessionDep):
    if not session.get(Videos, video_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Video no encontrado"
        )
    comentario = Comments(autor=data.autor, texto=data.texto, video_id=video_id)
    session.add(comentario)
    session.commit()
    session.refresh(comentario)
    return comentario
