from pydantic import BaseModel
from typing import List

class BlogBase(BaseModel):
    title: str
    body: str
    user_id: int

class Blog(BlogBase):
    class Config():
         orm_mode = True



class User(BaseModel):

    name: str
    email: str
    password: str

class ShowUserBase(BaseModel):

    name: str
    email: str

    class Config():
         orm_mode = True

class ShowUser(ShowUserBase):

    blogs : List[Blog] = []

    class Config():
         orm_mode = True




class ShowBlog(BaseModel):

    title: str
    body: str

    creator: ShowUserBase

    class Config():
         orm_mode = True         


class Login(BaseModel):

    username : str
    password: str         



class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None