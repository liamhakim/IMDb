import random
import shutil
import string
from fastapi import APIRouter, Depends, File, HTTPException, Query, UploadFile, status
from sqlalchemy.orm import Session
from typing import List, Optional
from db.database import SessionLocal
from router.schemas import MovieBase, MovieDisplay
from db import db_movie
from db.db_movie import create_movie, get_movie, update_movie, delete_movie
from db.database import get_db
from router.tmdb_service import get_movie_poster

router = APIRouter(prefix="/movie", tags=["movie"])


@router.post("", response_model=MovieDisplay)
def create_movie_endpoint(movie: MovieBase,category_id: int, db: Session = Depends(get_db)):
    created_movie = create_movie(db, movie, category_id)
    return created_movie

@router.get('', response_model=List[MovieDisplay])
def search_movies(title: Optional[str] = None,
    category: Optional[str] = None,
    director: Optional[str] = None,
    sort_by: Optional[str] = Query(None, description="Sort movies by 'year', 'title', 'rating', 'category'"),
    db: Session = Depends(get_db)
):
    return db_movie.search_movies(db,title=title, category=category, director=director, sort_by=sort_by)

@router.get("/{movie_id}", response_model=MovieDisplay)
def get_movie_endpoint(movie_id: int, db: Session = Depends(get_db)):
    movie = get_movie(db, movie_id)
    return movie

@router.get("/poster/{movie_id}")
def get_movie_poster_endpoint(movie_id: int):
    poster_url = get_movie_poster(movie_id)
    if poster_url:
        return {"poster_url": poster_url}
    else:
        return {"message": "Poster not found for the given movie ID"}

@router.get("/trailer/{movie_id}")

def get_movie_trailer_endpoint(movie_id: int):
    trailer_url = get_movie_trailer(movie_id)
    if trailer_url:
        return {"trailer_url": trailer_url}
    else:
        return {"message": "Trailer not found for the given movie ID"}



@router.put("/update/{movie_id}", response_model=MovieDisplay)
def update_movie_endpoint(movie_id: int, movie: MovieBase, db: Session = Depends(get_db)):
    updated_movie = update_movie(db, movie_id, movie)
    return updated_movie

@router.delete("/delete/{movie_id}")
def delete_movie_endpoint(movie_id: int, db: Session = Depends(get_db)):
    return delete_movie(db, movie_id)
       
@router.post('/image')
def upload_image(image: UploadFile = File(...)):
  letter = string.ascii_letters
  rand_str = ''.join(random.choice(letter) for i in range(6))
  new = f'_{rand_str}.'
  filename = new.join(image.filename.rsplit('.', 1))
  path = f'images/{filename}'

  with open(path, "w+b") as buffer:
    shutil.copyfileobj(image.file, buffer)

  return {'filename': path}

