from fastapi import FastAPI
from app.routes.account import router as account_router
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

B_app = FastAPI(title="Bank API")

B_app.include_router(account_router, prefix="/api/v1", tags=["Accounts"])
