from fastapi import FastAPI
from db.database import Base , engine
from router import movie, category, director, actor, user, rating, review
from auth import authentication
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.include_router(movie.router)
app.include_router(category.router)
app.include_router(director.router)
app.include_router(actor.router)
app.include_router(user.router)
app.include_router(authentication.router)
app.include_router(rating.router)
app.include_router(review.router)

app.add_middleware(

        CORSMiddleware,

        allow_origins=["*"],

        allow_credentials=True,

        allow_methods=["*"],

        allow_headers=["*"],      

    )

Base.metadata.create_all(engine) 
