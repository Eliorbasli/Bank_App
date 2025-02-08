from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.services.account_service import create_account, get_account
from app.schemas import AccountCreate, AccountResponse

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.post("/register" , response_model=AccountResponse)
def register_account(account: AccountCreate , db: Session = Depends(get_db)):
    return create_account(db,account)

@router.get("/account/{account_id}" , response_model=AccountResponse)
def account_status(account_id: int , db: Session = Depends(get_db)):
    acc = get_account(db, account_id)
    if not acc:
        return {"error" : "Account not found"}
    return acc