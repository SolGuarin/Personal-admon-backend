from sqlalchemy.orm import Session
from personal_finance import models
from personal_finance.schemas import TransactionCreateSchema, TransactionSchema


def get_transaction(db: Session, transaction_id: int):
    return db.query(models.Transaction).filter(models.Transaction.id == transaction_id).first()


def get_all_transaction(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Transaction).offset(skip).limit(limit).all()
