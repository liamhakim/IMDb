from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from typing import List
from db.database import SessionLocal
from router.schemas import MovieBase, MovieDisplay
from db import db_movie
from db.db_category import create_category, delete_category, get_movies_by_category, update_category
from router.schemas import CategoryDisplay, CategoryBase, MovieBase
from db.database import get_db
from db.models import DbCategory

router = APIRouter(prefix="/category", tags=["category"])


@router.post("", response_model=CategoryDisplay)
def create_category_endpoint(category: CategoryBase, db: Session = Depends(get_db)):
    created_category = create_category(db, category)
    return created_category


@router.get("/{category_id}/movies", response_model= List[MovieDisplay])
def get_movies_by_category_endpoint(category_id: int, db: Session= Depends(get_db)):    
    return get_movies_by_category(category_id,db)

@router.put('/{category_id}')
def update_category_endpoint (id: int, request: CategoryBase, db : Session=Depends(get_db)):
    return update_category(db, id, request)

@router.delete('/{category_id}')
def delete_category_endpoint(id: int, db : Session=Depends(get_db)):
    return delete_category(db, id)