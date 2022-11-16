from models import Movement, Account, Category, Transaction
import database


def run():
    pass


if __name__ == '__main__':
    database.Base.metadata.create_all(database.engine)
    run()
