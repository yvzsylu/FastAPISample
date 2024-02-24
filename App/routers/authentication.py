from fastapi import APIRouter,Depends,HTTPException,status
from .. import schemas,database,models,token
from sqlalchemy.orm import Session
from ..hashing import Hash
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(tags=['Authentication'],prefix="/login")





@router.post('/')

def login(request: OAuth2PasswordRequestForm = Depends(),db:Session = Depends(database.get_db)):

    user = db.query(models.User).filter(models.User.email == request.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Invalid Credentials")
    

    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Incorrect Password")
    
    #generate a jwt token and return


    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

    return 'login'
    