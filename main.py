from fastapi import FastAPI
from db.database import Base , engine
from router import movie, category, director, actor, user, rating
from auth import authentication

app = FastAPI()

app.include_router(movie.router)
app.include_router(category.router)
app.include_router(director.router)
app.include_router(actor.router)
app.include_router(user.router)
app.include_router(authentication.router)
app.include_router(rating.router)

Base.metadata.create_all(engine) 
print("Funk you")
