from sqlalchemy import Column, Float, ForeignKey, Integer, DECIMAL, String, Table
from db.database import Base
from sqlalchemy.orm import relationship

class DbCategory(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    movies = relationship("DbMovie", back_populates="category")

class DbDirector(Base):
    __tablename__ = "directors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    date_of_birth = Column(String)
    nationality = Column(String)
    movies = relationship("DbMovie", back_populates="director")

movie_actor_association = Table(
    'movie_actor',
    Base.metadata,
    Column('movie_id', Integer, ForeignKey('movies.id'), primary_key=True),
    Column('actor_id', Integer, ForeignKey('actors.id'), primary_key=True)
)

class DbMovie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    release_date = Column(String)
    plot_summary = Column(String)
    average_rating = Column(DECIMAL(8,1))
    category_id = Column(Integer, ForeignKey("categories.id"))
    director_id = Column(Integer, ForeignKey("directors.id")) 
    director = relationship("DbDirector", back_populates="movies")  
    category = relationship("DbCategory", back_populates="movies")
    actors = relationship("DbActor",secondary=movie_actor_association, back_populates="movies")
    ratings = relationship("DbRating", back_populates="movies")
    reviews = relationship("DbReview", back_populates="movie")

class DbActor(Base):
    __tablename__ = "actors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    date_of_birth = Column(String)
    nationality = Column(String)
    movies = relationship("DbMovie",secondary=movie_actor_association, back_populates="actors")



class DbReview(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    movie_id = Column(Integer, ForeignKey("movies.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    content = Column(String)
    
    movie = relationship("DbMovie", back_populates="reviews")
    user = relationship("DbUser", back_populates="reviews")




class DbUser(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    ratings = relationship("DbRating", back_populates="user") 
    reviews = relationship("DbReview", back_populates="user")


class DbRating(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True, index=True)
    movie_id = Column(Integer, ForeignKey("movies.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    rating_value = Column(Float)

    movies = relationship("DbMovie", back_populates="ratings")
    user = relationship("DbUser", back_populates="ratings")    