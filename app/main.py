from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models  
from .database import engine, SessionLocal
from .routers import post, user, auth,vote
from .config import settings
import os
import uvicorn 
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Default to 8000 if PORT is not set
    uvicorn.run("app.main:app", host="0.0.0.0", port=port, reload=True)
# print(settings.database_username)

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
 

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)
@app.get("/")
def root():

    return {"message": "Welcome to my API!!!"}





