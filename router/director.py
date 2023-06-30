from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.database import get_db
from db.db_director import create_director, get_movies_by_director, delete_director, update_director
from db.models import DbDirector
from router.schemas import DirectorDisplay, DirectorBase, MovieDisplay
router = APIRouter(prefix="/director", tags=["director"])


@router.post("", response_model=DirectorDisplay)
def create_director_endpoint(director: DirectorBase, db: Session = Depends(get_db)):
    created_director = create_director(db, director)
    return created_director

@router.get("/{director_id}/movies", response_model=List[MovieDisplay])
def get_movies_by_director_endpoint(director_id: int, db: Session= Depends(get_db)):
    return get_movies_by_director(director_id,db)
######################################################################

@router.put('/{id}', response_model=DirectorDisplay)
def update_director_endpoint (id: int, request: DirectorBase, db : Session=Depends(get_db)):
    return update_director(db, id, request)

@router.delete("/delete-director/{director_id}")
def delete_director_endpoint(director_id: int, db: Session = Depends(get_db)):
    return delete_director(db, director_id)