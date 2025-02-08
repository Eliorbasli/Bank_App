from sqlalchemy.orm import Session
from ..models import Account
from ..schemas import AccountCreate

def create_account(db: Session, account: AccountCreate):
    db_account = Account(owner_name=account.owner_name, balance=0.0)
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account

def get_account(db:Session , account_id:int):
    return db.query(Account).filter(Account.id == account_id).first()