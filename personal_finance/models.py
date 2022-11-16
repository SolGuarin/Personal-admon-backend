from sqlalchemy import Column, Integer, String, TIMESTAMP, BigInteger, Float
from personal_finance.database import Base


class Movement(Base):
    __tablename__ = "movement"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    account_id = Column(BigInteger)
    category_id = Column(BigInteger)
    note = Column(String(length=500))
    description = Column(String(length=500))
    from_account_id = Column(Integer)
    to_account_id = Column(BigInteger)
    type = Column(String(500))
    date = Column(TIMESTAMP)
    transaction_id = Column(BigInteger)
    transaction_equivalent_id = Column(BigInteger)


class Account(Base):
    __tablename__ = "account"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(500))
    type = Column(String(500))
    note = Column(String(500))


class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(500))
    type = Column(String(500))


class Transaction(Base):
    __tablename__ = "transaction"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    account = Column(String(500))
    description = Column(String(500))
    value = Column(Float)
    reference = Column(String(500))
    period = Column(String(500))
    billing_date = Column(String(500))
    source = Column(String(500))
    currency = Column(String(500))
    account_type = Column(String(500))
    balance = Column(String(500))
    branch_office = Column(String(500))
    channel_branch_office = Column(String(500))
    discount = Column(String(500))
    source_file = Column(String(500))
