from fastapi import HTTPException, status
from pydantic import BaseModel
from sqlalchemy.orm import Session
from db.models import DbCategory, DbMovie
from db.hashing import Hash
from router.helper import check_category
from router.schemas import CategoryDisplay, MovieBase, MovieDisplay


def create_category(db: Session, category: BaseModel):
    db_category = DbCategory(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category



def get_movies_by_category(category_id: int, db: Session):
    check_category(category_id,db)
    movies = db.query(DbMovie).filter(DbMovie.category_id == category_id).all()

    if not movies:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'no movies were found in category {category_id}')
    
    return movies
    
def update_category(db: Session,category_id: int, request: CategoryDisplay):

    check_category(category_id,db)
    db_category =db.query(DbCategory).filter(DbCategory.id==category_id)
    db_category.update({        
        DbCategory.name : request.name,
    })
    db.commit()
    db.refresh(db_category.first())
    return db_category.first()

def delete_category(db: Session, category_id: int):

    check_category(category_id,db)
    category= db.query(DbCategory).filter(DbCategory.id==category_id).first()
    db.delete(category)
    db.commit()
    return 'category has been deleted successfully'

