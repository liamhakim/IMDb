from fastapi import HTTPException, status
from db.models import DbUser
from router.helper import check_user
from router.schemas import UserBase
from sqlalchemy.orm import Session
from db.hashing import Hash

def Create_user(db: Session, request: UserBase):
  new_user = DbUser(
    username = request.username,
    email = request.email,
    password = Hash.bcrypt(request.password)
  )
  db.add(new_user)
  db.commit()
  db.refresh(new_user)
  return new_user

def get_user_by_username(db:Session, username: str):
  user = db.query(DbUser).filter(DbUser.username == username).first()
  if not user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f'user with username {username} not found')
  return user

def update_user(db: Session,id: int, request: UserBase):

    check_user(id,db)
    db_user =db.query(DbUser).filter(DbUser.id==id)
    db_user.update({        
        DbUser.username : request.username,
        DbUser.email  : request.email,
        DbUser.password : Hash.bcrypt(request.password)
    })
    db.commit()
    db.refresh(db_user.first())
    return db_user.first()

def delete_user(db: Session, id: int):
    check_user(id,db)
    user= db.query(DbUser).filter(DbUser.id==id).first()
    db.delete(user)
    db.commit()
    return 'user has been deleted successfully'

