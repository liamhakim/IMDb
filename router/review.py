from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from auth.oauth2 import get_current_user
from router.schemas import ReviewDisplay, ReviewBase, UserAuth
from db.database import get_db
from db.db_review import create_review

router = APIRouter(prefix="/reviews", tags=["reviews"])


@router.post("", response_model=ReviewDisplay)
def create_review_endpoint(review: ReviewBase, db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    return create_review(review, db, current_user.id)
