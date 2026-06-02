from fastapi import APIRouter, HTTPException, Response, Depends
from sqlalchemy.orm import Session
from typing import List

from app.schemas.user import UserCreate, UserResponse, UserUpdate
from app.models.user import User
from app.database import get_db

router = APIRouter()


@router.post("/users", status_code=201, response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(name=user.name, email=user.email, gender=user.gender, age=user.age)

    existing_user = db.query(User).filter(User.email == user.email).first()

    if existing_user:
        raise HTTPException(status_code=409, detail="Email already exists")

    db.add(db_user)
    db.commit()

    db.refresh(db_user)

    return db_user


@router.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user


@router.get("/users/", response_model=List[UserResponse])
def get_user(db: Session = Depends(get_db)):
    users = db.query(User).limit(10).all()

    return users


@router.patch("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, payload: UserUpdate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if payload.name is not None:
        user.name = payload.name

    if payload.email is not None:
        existing_user = (
            db.query(User)
            .filter(User.email == payload.email, User.id != user_id)
            .first()
        )

        if existing_user:
            raise HTTPException(status_code=409, detail="Email already exists")
        user.email = payload.email

    if payload.gender is not None:
        user.gender = payload.gender

    if payload.age is not None:
        user.age = payload.age

    db.commit()
    db.refresh(user)

    return user


@router.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()

    return Response(status_code=204)
