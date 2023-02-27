from fastapi import FastAPI
from database.config import database, metadata, engine
from app.api import app_router
from auth.api import auth_api


app = FastAPI()




app.include_router(app_router)
app.include_router(auth_api)




metadata.create_all(engine)
app.state.database = database




# app.include_router(api_router)
@app.on_event("startup")
async def startup() -> None:
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()





@app.on_event("shutdown")
async def shutdown() -> None:
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()