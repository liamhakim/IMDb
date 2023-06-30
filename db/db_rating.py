from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from router.helper import check_rating
from router.schemas import RatingCreate
from db.models import DbRating, DbMovie, DbUser

def create_rating( rating: RatingCreate, db: Session , user_id: int ):
    movie = db.query(DbMovie).filter(DbMovie.id == rating.movie_id).first()
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")

    db_rating = DbRating(
       movie_id=rating.movie_id,
       user_id= user_id,
       rating_value=rating.rating_value
       )
    db.add(db_rating)
    db.commit()
    db.refresh(db_rating)

    return db_rating

def update_rating(db: Session,id: int, request: create_rating, user_id: int):

    check_rating(id,db)

    db_rating =db.query(DbRating).filter(DbRating.id==id)
    if user_id != db_rating.first().user_id:
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND, detail= 'not legal user')

    db_rating.update({        
       DbRating.rating_value : request.rating_value,
    })
    db.commit()
    db.refresh(db_rating.first())
    return db_rating.first()

def delete_rating (db: Session, director_id: int, user_id: int):
    rating = db.query(DbRating).filter(DbRating.id == director_id).first()
    if user_id != rating.user_id:
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND, detail= 'not legal user')
    if not rating:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No rating were found")
    db.delete(rating)
    db.commit()
    return {"message": "rating has been deleted"}
    

