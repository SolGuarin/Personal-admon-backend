from datetime import date
from typing import Optional

from pydantic import BaseModel
from pydantic import Field

# schemas category


class CategoryCreateSchema(BaseModel):
    name: str = Field(
        ...,
        min_length=1,
        max_length=500
    )
    type: str = Field(
        ...,
        min_length=1,
        max_length=500
    )


class CategorySchema(CategoryCreateSchema):
    id: int = Field(
        ...
    )

    class Config:
        orm_mode = True

# schema account


class AccountCreateSchema(BaseModel):
    name: str = Field(
        ...
    )
    type: str = Field(
        ...
    )
    note: Optional[str] = Field(

    )


class AccountSchema(AccountCreateSchema):
    id: int = Field(
        ...
    )

    class Config:
        orm_mode = True

# schema transaction


class TransactionCreateSchema(BaseModel):
    account: str = Field()
    description: str = Field()
    value: float = Field()
    reference: str = Field()
    period: str = Field()
    billing_date: str = Field()
    source: str = Field()
    currency: str = Field()
    account_type: str = Field()
    balance: str = Field()
    branch_office: str = Field()
    channel_branch_office: str = Field()
    discount: str = Field()
    source_file: str = Field()


class TransactionSchema(TransactionCreateSchema):
    id: int = Field(
        ...
    )

    class Config:
        orm_mode = True

# schema movement


class MovementCreateSchema(BaseModel):
    account_id: int = Field()
    category_id: int = Field()
    note: str = Field()
    description: str = Field()
    from_account_id: int = Field()
    to_account_id: int = Field()
    type: str = Field()
    date: str = Field()
    transaction_id: int = Field()
    transaction_equivalent_id: int = Field()


class MovementSchema(MovementCreateSchema):
    id: int = Field(
        ...
    )
