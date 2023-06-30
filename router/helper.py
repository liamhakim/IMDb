from sqlalchemy.orm import Session
from fastapi import HTTPException
from db.models import DbActor, DbCategory, DbDirector, DbRating, DbUser, DbMovie


def check_user(user_id: int, db: Session) -> bool:

    user = db.query(DbUser).filter(DbUser.id == user_id).first()

    if not user:

        raise HTTPException(status_code=404, detail="User not found")

    return True

def check_category(category_id: int, db: Session) -> bool:

    category = db.query(DbCategory).filter(DbCategory.id == category_id).first()

    if not category:

        raise HTTPException(status_code=404, detail="category not found")

    return True


def check_movie(movie_id: int, db: Session) -> bool:

    movie = db.query(DbMovie).filter(DbMovie.id == movie_id).first()

    if not movie:

        raise HTTPException(status_code=404, detail="movie not found")

    return True

def check_director(director_id: int, db: Session) -> bool:

    director = db.query(DbDirector).filter(DbDirector.id == director_id).first()

    if not director:

        raise HTTPException(status_code=404, detail="director not found")

    return True

def check_actor(actor_id: int, db: Session) -> bool:

    actor = db.query(DbActor).filter(DbActor.id == actor_id).first()

    if not actor:

        raise HTTPException(status_code=404, detail="actor not found")

    return True

def check_rating(rating_id: int, db: Session) -> bool:

    rating = db.query(DbRating).filter(DbRating.id == rating_id).first()

    if not rating:

        raise HTTPException(status_code=404, detail="there is no rating found")

    return True