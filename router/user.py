from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from router.schemas import UserBase, UserDisplay
from db.db_user import Create_user, delete_user, update_user

router = APIRouter(
    prefix='/user',
    tags=['user']
)

@router.post ('', response_model=UserDisplay)
def create_user_endpoint (request: UserBase, db: Session = Depends (get_db)):
    return Create_user(db, request)

@router.put('/{id}', response_model=UserDisplay)
def update_user_endpoint (id: int, request: UserBase, db : Session=Depends(get_db)):
    return update_user(db, id, request)

@router.delete('/{id}')
def delete_user_endpoint(id: int, db : Session=Depends(get_db)):
    return delete_user(db, id)