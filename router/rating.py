from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from auth.oauth2 import get_current_user
from db.database import get_db
from router.schemas import RatingDisplay, RatingCreate, UserAuth
from db.db_rating import create_rating, delete_rating, update_rating

router = APIRouter(prefix="/ratings", tags=["ratings"])

@router.post("")
def create_rating_endpoint(rating: RatingCreate, db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    return create_rating(rating, db, current_user.id)

@router.put('/{id}', response_model=RatingDisplay)
def update_rating_endpoint (id: int, request: RatingCreate, db : Session=Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    return update_rating(db, id, request,current_user.id)

@router.delete("/delete/{rating_id}")
def delete_rating_endpoint(rating_id: int, db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    return delete_rating(db, rating_id, current_user.id)