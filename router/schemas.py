from pydantic import BaseModel
from typing import List, Optional

class ActorBase(BaseModel):
    name: str
    date_of_birth: str
    nationality: str
    

class ActorMovie(BaseModel):
    id: int

class MovieBase(BaseModel):
    title: str
    release_date: str
    plot_summary: str
    director_id: int
    actors: List[ActorMovie] 

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
    title: str
    release_date: str
    average_rating: Optional[int]
    category: Optional[CategoryForMovie]
    director: Optional [DirectorforMovie]
    class Config:
        orm_mode = True

class CategoryBase(BaseModel):
    name: str

class CategoryDisplay(BaseModel):
    id: int
    name: str
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

class UserDisplay(BaseModel):
     username: str
     email: str
     
     class Config:
        orm_mode = True

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
