from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from db.models import DbActor
from router.helper import check_actor
from router.schemas import ActorBase

def create_actor(db: Session, actor: ActorBase):
    new_actor = DbActor(
        name=actor.name, 
        date_of_birth=actor.date_of_birth, 
        nationality=actor.nationality
        )
    db.add(new_actor)
    db.commit()
    db.refresh(new_actor)
    return new_actor

def update_actor(db: Session,actor_id: int, request: ActorBase):

    check_actor(actor_id,db)
    db_actor =db.query(DbActor).filter(DbActor.id==actor_id)
    db_actor.update({        
        DbActor.name : request.name,
        DbActor.nationality  : request.nationality,
        DbActor.date_of_birth : request.date_of_birth
    })
    db.commit()
    db.refresh(db_actor.first())
    return db_actor.first()

def delete_actor (db: Session, actor_id: int):
    check_actor(actor_id,db)
    actor = db.query(DbActor).filter(DbActor.id == actor_id).first()
    if actor:
        db.delete(actor)
        db.commit()
        return {"message": "Actor deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="actor not found")

