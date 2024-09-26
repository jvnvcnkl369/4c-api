from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional, Sequence
from app.database import get_db
from app.models import models

from app.schemas import Post
from app.schemas.post import PostStatus
from app.utils import apply_includes

router = APIRouter()


@router.get("/api/posts", response_model=None, response_model_exclude_unset=True)
def get_posts(
    status: Optional[str] = None,
    include: Optional[str] = Query(None),
    db: Session = Depends(get_db),
) -> Sequence[Post]:
    query = db.query(models.Post)
    if status and status in PostStatus:
        query = query.filter(models.Post.status == status)

    query = apply_includes(query, models.Post, include)
    posts = query.all()

    return posts


@router.get(
    "/api/posts/{post_id}", response_model=None, response_model_exclude_unset=True
)
def get_post(
    post_id: int, include: Optional[str] = Query(None), db: Session = Depends(get_db)
) -> Post:
    query = db.query(models.Post).filter(models.Post.id == post_id)
    query = apply_includes(query, models.Post, include)

    post = query.first()
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post
