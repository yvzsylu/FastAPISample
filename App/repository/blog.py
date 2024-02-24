from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from .. import models,schemas


def get_all(db:Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create(request:schemas.Blog,db:Session):

    user = db.query(models.User).filter(models.User.id == request.user_id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with the {request.user_id} is not available")

    new_blog = models.Blog(title=request.title,body=request.body,user_id = request.user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog


def destroy(id:int,db:Session):
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return 'Done.'


def update(id:int,request:models.Blog,db:Session):

    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with the {id} is not available")

    blog.update(request.model_dump())

    db.commit()

    return 'Updated.'

def show(id:int,db:Session):

    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with the {id} is not available")
    
    return blog
