from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional
from app.database import get_db
from app.models import models
from app.schemas import User
from app.utils import apply_includes

router = APIRouter()


@router.get(
    "/api/users/{user_id}", response_model=None, response_model_exclude_unset=True
)
def get_user(
    user_id: int, include: Optional[str] = Query(None), db: Session = Depends(get_db)
) -> User:

    query = db.query(models.User).filter(models.User.id == user_id)
    query = apply_includes(query, models.User, include)
    user = query.first()

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return user
