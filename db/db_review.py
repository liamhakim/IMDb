from fastapi import HTTPException
from sqlalchemy.orm import Session
from router.helper import check_movie
from db.models import DbMovie, DbReview
from router.schemas import ReviewBase


def create_review(review: ReviewBase,db: Session, user_id: int):
    movie = db.query(DbMovie).filter(DbMovie.id == review.movie_id).first()
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    db_review = DbReview(
       movie_id=review.movie_id,
       user_id=user_id,
       content =review.content
       )
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review
