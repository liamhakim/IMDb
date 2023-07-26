from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class UserDisplay(BaseModel):
     id: int
     username: str
     email: str
     
     class Config:
        orm_mode = True


class ReviewBase(BaseModel):
    movie_id: int
    content: str

class ReviewDisplay(BaseModel):
    id: int
    user: UserDisplay
    content: str
    date: datetime
    class Config:
        orm_mode = True

class ActorBase(BaseModel):
    name: str
    date_of_birth: str
    nationality: str
    

class ActorMovie(BaseModel):
    id: int


class ActorRating(BaseModel):
    id: int
    average_rating: float
    class Config:
        orm_mode = True

class MovieBase(BaseModel):
    image_url: str
    title: str
    release_date: str
    plot_summary: str
    director_id: int
    actors: List[ActorMovie] 
    average_rating: float
    

class CategoryForMovie(BaseModel):
    id: int
    name: str
    class Config:
        orm_mode = True

class DirectorforMovie(BaseModel):
    name: str
    class Config:
        orm_mode = True

class MovieDisplay(BaseModel):
    id: int
    #image_url: str
    title: str
    release_date: str
    average_rating: Optional[int]
    category: Optional[CategoryForMovie]
    director: Optional [DirectorforMovie]
    #trailer: Optional[str]
    poster_url: str
    trailer_url: str
    plot_summary: str
    reviews: List[ReviewDisplay]
    class Config:
        orm_mode = True

class CategoryBase(BaseModel):
    name: str
    tmdb: int

class CategoryDisplay(BaseModel):
    id: int
    name: str
    tmdb: int 
    movies: list[MovieDisplay]

    class Config:
        orm_mode = True


class DirectorBase(BaseModel):
    name: str
    date_of_birth: str
    nationality: str

class DirectorDisplay(BaseModel):
    id: int
    name: str
    movies: list[MovieDisplay]

    class Config:
        orm_mode = True


class ActorDisplay(BaseModel):
    id: int
    name: str
    movies: list[MovieDisplay]

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str
    email: str
    password: str


class UserAuth(BaseModel):
    id: int
    username:str
    email: str

class RatingCreate(BaseModel):
    movie_id: int
    rating_value: float

class RatingDisplay(BaseModel):
    id: int
    movie_id: int
    user_id: int
    rating_value: float

    class Config:
        orm_mode = True
