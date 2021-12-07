from sqlalchemy.orm import Session, session
from sqlalchemy.future import select
import models


# def get_user(db: Session, user_id: int):
#     return db.query(models.User).filter(models.User.id == user_id).first()


# def get_user_by_email(db: Session, email: str):
#     return db.query(models.User).filter(models.User.email == email).first()


# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.User).offset(skip).limit(limit).all()


def create_certificates(db: Session, data):
    certificates = [models.Certificates(*cert) for cert in data]
    db.add_all(certificates)
    db.commit()
    return 

def get_certificate_by_name(db: Session, issue_to: str):
    q = select(models.Certificates).where(models.Certificates.issued_to == issue_to)
    return db.scalar(q)

# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()


# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item