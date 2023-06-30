
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from db.database import get_db
from db.db_actor import create_actor, delete_actor, update_actor
from router.schemas import ActorBase, ActorDisplay


router = APIRouter(prefix="/actor", tags=["actor"])


@router.post("", response_model=ActorDisplay)
def create_actor_endpoint(actor: ActorBase, db: Session = Depends(get_db)):
     return create_actor(db, actor)
     

@router.put('/{id}', response_model=ActorDisplay)
def update_actor_endpoint (id: int, request: ActorBase, db : Session=Depends(get_db)):
    return update_actor(db, id, request)

@router.delete("/delete-actor/{actor_id}")
def delete_actor_endpoint(actor_id: int, db: Session = Depends(get_db)):
    return delete_actor(db, actor_id)