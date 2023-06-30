from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.models import DbDirector, DbMovie
from router.helper import check_director
from router.schemas import DirectorBase, MovieDisplay, UserBase

def create_director(db: Session, director: DirectorBase):
    new_director = DbDirector(
        name=director.name,
        date_of_birth=director.date_of_birth,
        nationality=director.nationality)
    
    db.add(new_director)
    db.commit()
    db.refresh(new_director)
    return new_director

def get_movies_by_director(director_id: int, db: Session):
    check_director(director_id, db)
    movies = db.query(DbMovie).filter(DbMovie.director_id == director_id).all()

    if not movies:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No movies were found for director with id {director_id}')
    
    return movies

def update_director(db: Session,director_id: int, request: DirectorBase):

    check_director(director_id,db)
    db_director =db.query(DbDirector).filter(DbDirector.id==director_id)
    db_director.update({        
        DbDirector.name : request.name,
        DbDirector.nationality  : request.nationality,
        DbDirector.date_of_birth : request.date_of_birth
    })
    db.commit()
    db.refresh(db_director.first())
    return db_director.first()

def delete_director (db: Session, director_id: int):
    check_director(director_id,db)
    director = db.query(DbDirector).filter(DbDirector.id == director_id).first()
    if director:
        db.delete(director)
        for movie in director.movies:
            db.delete(movie)
        db.commit()
        return {"message": "Director and associated movies deleted successfully"}


