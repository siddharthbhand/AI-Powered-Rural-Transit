from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate, UserLogin
from app.core.security import hash_password


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_user_by_phone(db: Session, phone: str):
    return db.query(User).filter(User.phone == phone).first()


def create_user(db: Session, user: UserCreate):
    hashed_pwd = hash_password(user.password)

    db_user = User(
        full_name=user.full_name,
        email=user.email,
        phone=user.phone,
        hashed_password=hashed_pwd,
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

def authenticate_user(db: Session, user: UserLogin):
    db_user = get_user_by_email(db, user.email)

    if not db_user:
        return None

    from app.core.security import verify_password

    if not verify_password(user.password, db_user.hashed_password):
        return None

    return db_user