from fastapi import HTTPException, status
from pydantic import BaseModel
from sqlalchemy.orm import Session
from db.models import DbActor, DbCategory, DbMovie, movie_actor_association, DbDirector
from router.schemas import MovieBase, MovieDisplay
from router.helper import check_movie
from typing import Optional
from router.helper import check_actor,check_director,check_category
from sqlalchemy import desc
from router.tmdb_service import get_movie_poster, get_movie_trailer, get_trending_movies
from db.database import SessionLocal

def create_movie(db: Session, movie: MovieBase, category_id: int):
    
    poster= get_movie_poster(movie.title)
    movie_key = get_movie_trailer(poster['trailer_id'])
    trailer_url = f'https://www.youtube.com/watch?v={movie_key}'
    print(trailer_url)
    
    new_movie = DbMovie(
        title=movie.title, 
        release_date=movie.release_date, 
        plot_summary=movie.plot_summary, 
        category_id=category_id,
        director_id=movie.director_id,
        poster_url= poster['image_url'],
        trailer_url= trailer_url,
        average_rating=movie.average_rating
        )
    
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    
    for actor in movie.actors:

        new_association = movie_actor_association.insert().values(movie_id=new_movie.id, actor_id=actor.id)
        db.execute(new_association)
    
    db.commit()
    return new_movie
###################################
def store_trending_movies_in_database():
    # Fetch trending movies from TMDB
    trending_movies = get_trending_movies()
    
    # Open a database session
    db = SessionLocal()
    
    try:
        # Loop through the trending movies and store them in the database
        for movie in trending_movies:
            # Create a new movie in the database
            create_movie(db, movie)
        
        # Commit the changes to the database
        db.commit()
    except Exception as e:
        # Rollback the transaction if an error occurs
        db.rollback()
        raise e
    finally:
        # Close the database session
        db.close()
###################################
 

def get_movie(db: Session, movie_id: int):
    movie= db.query(DbMovie).filter(DbMovie.id == movie_id).first()

    if not movie:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "Movie not found")
 
    return movie

def update_movie(db: Session, movie_id: int, movie: MovieBase):
   check_movie(movie_id,db)
   db_movie = db.query(DbMovie).filter(DbMovie.id == movie_id).first()
   if db_movie:
       db_movie.title = movie.title
       db_movie.release_date = movie.release_date
       db_movie.plot_summary = movie.plot_summary
       db.add(db_movie)
       db.commit()
       db.refresh(db_movie)
   return db_movie

def delete_movie(db: Session, movie_id: int):
    check_movie(movie_id,db)
    db_movie = db.query(DbMovie).filter(DbMovie.id == movie_id).first()
    if db_movie:
        db.delete(db_movie)
        db.commit()
        return {"message": "Movie deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "Movie not found")


def search_movies(db: Session, title: Optional[str]= None,category: Optional[str] = None, director: Optional[str] = None, sort_by: Optional[str] = None):
    query = db.query(DbMovie)
    if title:
        query = query.filter(DbMovie.title.ilike(f'%{title}%'))
    if category:
        query = query.join(DbCategory, DbMovie.category_id == DbCategory.id).filter(DbCategory.name.ilike(f'%{category}%'))
    if director:
        query = query.join(DbDirector, DbMovie.director_id == DbDirector.id).filter(DbDirector.name.ilike(f'%{director}%'))
   
    if sort_by:
        if sort_by == "year":
            query = query.order_by(DbMovie.release_date)
        elif sort_by == "title":
            query = query.order_by(DbMovie.title)
        elif sort_by == "rating":
            query = query.order_by(DbMovie.average_rating.desc())
        elif sort_by == "category":
            query = query.join(DbCategory, DbMovie.category_id == DbCategory.id).order_by(DbCategory.name)
    
    
    
    movies = query.all()
    return movies




