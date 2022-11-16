from sqlalchemy.orm import Session

from personal_finance import models
from personal_finance.schemas import CategoryCreateSchema, CategorySchema


def create_category(db: Session, category: CategoryCreateSchema):
    db_item = models.Category(**category.dict())
    db.add(db_item)
    db.commit()
    return db_item


def get_category(db: Session, category_id: int):
    return db.query(models.Category).filter(models.Category.id == category_id).first()


def update_category(db: Session, category: CategorySchema):
    db.query(models.Category).filter(models.Category.id == category.id).update(category.dict())
    db.commit()


def delete_category(db: Session, category_id: int):
    db_item = db.query(models.Category).filter(models.Category.id == category_id).first()
    db.delete(db_item)
    db.commit()
