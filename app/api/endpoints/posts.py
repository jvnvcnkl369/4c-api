from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.database import get_db
from app.models import models

from app.schemas import Post
from app.schemas.post import Post, PostStatus
from app.utils import apply_includes

router = APIRouter()


@router.get(
    "/api/posts",
    response_model=List[Post],
    response_model_exclude_defaults=True,
    status_code=200,
)
def get_posts(
    status: Optional[str] = None,
    include: Optional[str] = Query(None),
    db: Session = Depends(get_db),
):
    query = db.query(models.Post)

    if status and status in [enum.value for enum in PostStatus]:
        query = query.filter(models.Post.status == status)

    query = apply_includes(query, models.Post, include)

    return query.all()


@router.get(
    "/api/posts/{post_id}",
    response_model=Post,
    response_model_exclude_defaults=True,
    status_code=200,
)
def get_post(
    post_id: int, include: Optional[str] = Query(None), db: Session = Depends(get_db)
):
    query = db.query(models.Post).filter(models.Post.id == post_id)
    query = apply_includes(query, models.Post, include)
    post = query.first()

    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")

    return post
