from datetime import datetime

from pydantic import BaseModel
from pydantic.schema import Optional


class OrmBaseModel(BaseModel):
    class Config:
        orm_mode = True


class UserBaseSchema(OrmBaseModel):
    first_name: str
    last_name: str
    profile_name: str
    email: str
    country: str


class UserCreateSchema(UserBaseSchema):
    password: str


class UserGetSchema(UserBaseSchema):
    id: int
    signup_date: datetime


class UserUpdateSchema(OrmBaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    profile_name: Optional[str]
    email: Optional[str]
    country: Optional[str]


class UserFollowingSchema(OrmBaseModel):
    user_id: int
    follower_id: int
    followed_at: datetime


class UserBlogSchema(OrmBaseModel):
    user_id: int
    blog_id: int


class InteractionSchema(OrmBaseModel):
    user_id: int
    content_id: int
    interacted_with_at: datetime


class BlogBaseSchema(OrmBaseModel):
    title: str
    description: str


class BlogCreateSchema(BlogBaseSchema):
    pass


class BlogGetSchema(BlogCreateSchema):
    id: str
    created_at: datetime


class BlogUpdateSchema(OrmBaseModel):
    title: Optional[str]
    description: Optional[str]


class PostBaseSchema(OrmBaseModel):
    blog_id: int
    title: str
    body: str


class PostCreateSchema(PostBaseSchema):
    pass


class PostGetSchema(PostBaseSchema):
    id: int
    created_at: datetime


class PostUpdateSchema(OrmBaseModel):
    title: Optional[str]
    body: Optional[str]


class CommentBaseSchema(OrmBaseModel):
    user_id: int
    post_id: int
    body: str


class CommentCreateSchema(CommentBaseSchema):
    pass


class CommentGetSchema(CommentBaseSchema):
    id: int
    created_at: datetime


class CommentUpdateSchema(OrmBaseModel):
    body: Optional[str]
