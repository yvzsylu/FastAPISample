from fastapi import APIRouter,Depends,status,HTTPException
from .. import schemas,models,oaut2
from App.database import get_db
from sqlalchemy.orm import Session
from App.hashing import Hash
from .. repository import user


router = APIRouter(
    prefix = "/user",
    tags=['Users']
)



@router.post('/',status_code=status.HTTP_201_CREATED,response_model=schemas.ShowUser)

def create_user(request:schemas.User,db : Session = Depends(get_db),current_user:schemas.User = Depends(oaut2.get_current_user)):

    return user.create(request,db)


@router.get('/{id}',response_model=schemas.ShowUser)

def get_user(id:int,db : Session = Depends(get_db),current_user:schemas.User = Depends(oaut2.get_current_user)):

    return user.show(id,db)