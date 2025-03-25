from sqlalchemy.orm import Session
from warehouse_management.domain.unit_of_work import UnitOfWork

class SqlAlchemyUnitOfWork(UnitOfWork):
    def __init__(self, session: Session):
        self.session=session

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.rollback()
        self.session.close()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
