from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from typing import List, Optional
from db.database import SessionLocal
from router.schemas import MovieBase, MovieDisplay
from db import db_movie
from db.db_movie import create_movie, get_movie, update_movie, delete_movie
from db.database import get_db

router = APIRouter(prefix="/movie", tags=["movie"])


@router.post("", response_model=MovieDisplay)
def create_movie_endpoint(movie: MovieBase,category_id: int, db: Session = Depends(get_db)):
    created_movie = create_movie(db, movie, category_id)
    return created_movie

@router.get('', response_model=List[MovieDisplay])
def search_movies(title: Optional[str] = None, category: Optional[str] = None, director: Optional[str] = None, db: Session = Depends(get_db)):
     return db_movie.search_movies(db,title=title, category=category, director=director)

@router.get("/{movie_id}", response_model=MovieDisplay)
def get_movie_endpoint(movie_id: int, db: Session = Depends(get_db)):
    movie = get_movie(db, movie_id)
    return movie

@router.put("/update/{movie_id}", response_model=MovieDisplay)
def update_movie_endpoint(movie_id: int, movie: MovieBase, db: Session = Depends(get_db)):
    updated_movie = update_movie(db, movie_id, movie)
    return updated_movie

@router.delete("/delete/{movie_id}")
def delete_movie_endpoint(movie_id: int, db: Session = Depends(get_db)):
    return delete_movie(db, movie_id)
       


