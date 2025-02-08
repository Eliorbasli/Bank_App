from fastapi import FastAPI
from .routes.account import router as account_router
from .database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Bank API")

app.include_router(account_router, prefix="/api/v1", tags=["Accounts"])
