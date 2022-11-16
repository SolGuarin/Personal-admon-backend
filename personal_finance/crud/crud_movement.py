from sqlalchemy.orm import Session

from personal_finance import models
from personal_finance.schemas import MovementCreateSchema, MovementSchema


def create_movement(db: Session, movement: MovementCreateSchema):
    db_item = models.Movement(**movement.dict())
    db.add(db_item)
    db.commit()
    return db_item


def get_movement(db: Session, movement_id: int):
    return db.query(models.Movement).filter(models.Movement.id == movement_id).first()


def update_movement(db: Session, movement: MovementSchema):
    db.query(models.Movement).filter(models.Movement.id == movement.id).update(movement.dict())
    db.commit()


def delete_movement(db: Session, movement_id: int):
    db_item = db.query(models.Movement).filter(models.Movement.id == movement_id).first()
    db.delete(db_item)
    db.commit()
