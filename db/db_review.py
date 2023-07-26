from fastapi import HTTPException
from sqlalchemy.orm import Session
from router.helper import check_movie
from db.models import DbMovie, DbReview
from router.schemas import ReviewBase
from datetime import datetime


def create_review(review: ReviewBase,db: Session, user_id: int):
    movie = db.query(DbMovie).filter(DbMovie.id == review.movie_id).first()
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    db_review = DbReview(
       movie_id=review.movie_id,
       user_id=user_id,
       content =review.content,
       date=datetime.now()
       )
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

def delete_review(review_id: int, db: Session, user_id: int):
    review = db.query(DbReview).filter(DbReview.id == review_id).first()
    if not review:
        return None  # Review not found, return None or raise an HTTPException with status_code=404

    # Check if the authenticated user is the owner of the review
    if review.user_id != user_id:
        raise HTTPException(status_code=403, detail="Permission denied. You are not the owner of this review.")

    db.delete(review)
    db.commit()
    return {"message": "Review deleted successfully"}
    return review
