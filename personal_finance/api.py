from fastapi import Depends, HTTPException, FastAPI, Body
from sqlalchemy.orm import Session
from starlette import status

from personal_finance.crud import crud_category, crud_account, crud_transaction, crud_movement
from personal_finance.database import SessionLocal
from personal_finance.schemas import CategoryCreateSchema, CategorySchema, AccountCreateSchema, AccountSchema, MovementCreateSchema, MovementSchema

app = FastAPI()


# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# endpoints de usuarios


@app.get(
    path="/",
    status_code=status.HTTP_200_OK,
    tags=["Home"]
)
def home():
    return {"input": "personal finance app..."}


# endpoints categories


@app.post(
    path="/categories",
    status_code=status.HTTP_201_CREATED,  # porque es para crear una persona
    tags=["categories"],
    summary="create category in the app"
)
def create_category(category: CategoryCreateSchema = Body(...), db: Session = Depends(get_db)):
    """
    Create User

    This path operation creates a user in the app and save the information in the database

    Parameters:
        -Request body parameter:
            -**usuario: UsuariosCreateSchema** -> A usuario model with login, password, nickname and email
    """
    crud_category.create_category(db=db, category=category)


@app.get(
    path="/categories/{category_id}",
    status_code=status.HTTP_200_OK,
    tags=["categories"]
)
def read_category(category_id: int, db: Session = Depends(get_db)):
    db_category = crud_category.get_category(db, category_id=category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_category


@app.put(
    path="/categories",
    status_code=status.HTTP_200_OK,  # porque es para crear una persona
    tags=["categories"],
    summary="update category in the app"
)
def update_category(category: CategorySchema = Body(...), db: Session = Depends(get_db)):
    """
    Soleny your homework is to fill up the documentation
    """
    crud_category.update_category(db=db, category=category)


@app.delete(
    path="/categories/{category_id}",
    status_code=status.HTTP_200_OK,
    tags=["categories"],
    summary="delete category in the database"
)
def delete_usuario(category_id: int, db: Session = Depends(get_db)):
    crud_category.delete_category(db=db, category_id=category_id)


# endpoints account


@app.post(
    path="/accounts",
    status_code=status.HTTP_201_CREATED,  # porque es para crear una persona
    tags=["account"],
    summary="create account in the app"
)
def create_account(account: AccountCreateSchema = Body(...), db: Session = Depends(get_db)):
    """
    Create User

    This path operation creates a user in the app and save the information in the database

    Parameters:
        -Request body parameter:
            -**usuario: UsuariosCreateSchema** -> A usuario model with login, password, nickname and email
    """
    crud_account.create_account(db=db, account=account)


@app.get(
    path="/accounts/{account_id}",
    status_code=status.HTTP_200_OK,
    tags=["account"]
)
def read_account(account_id: int, db: Session = Depends(get_db)):
    db_account = crud_account.get_account(db, account_id=account_id)
    if db_account is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_account


@app.put(
    path="/accounts",
    status_code=status.HTTP_200_OK,  # porque es para crear una persona
    tags=["account"],
    summary="update account in the app"
)
def update_account(account: AccountSchema = Body(...), db: Session = Depends(get_db)):
    """
    Soleny your homework is to fill up the documentation
    """
    crud_account.update_account(db=db, account=account)


@app.delete(
    path="/accounts/{account_id}",
    status_code=status.HTTP_200_OK,
    tags=["account"],
    summary="delete account in the database"
)
def delete_usuario(account_id: int, db: Session = Depends(get_db)):
    crud_account.delete_account(db=db, account_id=account_id)

# endpoints transaction


@app.get(
    path="/transactions/{transaction_id}",
    status_code=status.HTTP_200_OK,
    summary="show a transaction in the app ",
    tags=["transactions"]
)
def read_transaction(transaction_id: int, db: Session = Depends(get_db)):
    db_transaction = crud_transaction.get_transaction(db, transaction_id=transaction_id)
    if db_transaction is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_transaction


@app.get(
    path="/transactions",
    status_code=status.HTTP_200_OK,
    summary="show all transactions in the database ",
    tags=["transactions"]
)
def read_all_transaction(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_transaction = crud_transaction.get_all_transaction(db, skip=skip, limit=limit)
    if db_transaction is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_transaction


# endpoints movement

@app.post(
    path="/movements",
    status_code=status.HTTP_201_CREATED,  # porque es para crear una persona
    tags=["movements"],
    summary="create a movement in the app"
)
def create_movement(movement: MovementCreateSchema = Body(...), db: Session = Depends(get_db)):
    """
    Create User

    This path operation creates a user in the app and save the information in the database

    Parameters:
        -Request body parameter:
            -**usuario: UsuariosCreateSchema** -> A usuario model with login, password, nickname and email
    """
    crud_movement.create_movement(db=db, movement=movement)


@app.get(
    path="/movements/{movement_id}",
    status_code=status.HTTP_200_OK,
    tags=["movements"]
)
def read_movement(movement_id: int, db: Session = Depends(get_db)):
    db_movement = crud_movement.get_movement(db, movement_id=movement_id)
    if db_movement is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_movement


@app.put(
    path="/movements",
    status_code=status.HTTP_200_OK,  # porque es para crear una persona
    tags=["movements"],
    summary="update movement in the app"
)
def update_movement(movement: MovementSchema = Body(...), db: Session = Depends(get_db)):
    """
    Soleny your homework is to fill up the documentation
    """
    crud_movement.update_movement(db=db, movement=movement)


@app.delete(
    path="/movements/{movement_id}",
    status_code=status.HTTP_200_OK,
    tags=["movements"],
    summary="delete movement in the database"
)
def delete_movement(movement_id: int, db: Session = Depends(get_db)):
    crud_movement.delete_movement(db=db, movement_id=movement_id)

