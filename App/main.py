from fastapi import FastAPI,Depends,Response,status,HTTPException
from typing import List
from . import schemas,models
from App.database import engine,get_db
from sqlalchemy.orm import Session
from .hashing import Hash
from .routers import blog,user,authentication
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get("/")
async def docs_redirect():
    return RedirectResponse(url='/docs')

models.Base.metadata.create_all(engine)



app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)




    




