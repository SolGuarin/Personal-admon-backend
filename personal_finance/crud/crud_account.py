from sqlalchemy.orm import Session

from personal_finance import models
from personal_finance.schemas import AccountCreateSchema, AccountSchema


def create_account(db: Session, account: AccountCreateSchema):
    db_item = models.Account(**account.dict())
    db.add(db_item)
    db.commit()
    return db_item


def get_account(db: Session, account_id: int):
    return db.query(models.Account).filter(models.Account.id == account_id).first()


def update_account(db: Session, account: AccountSchema):
    db.query(models.Account).filter(models.Account.id == account.id).update(account.dict())
    db.commit()


def delete_account(db: Session, account_id: int):
    db_item = db.query(models.Account).filter(models.Account.id == account_id).first()
    db.delete(db_item)
    db.commit()
