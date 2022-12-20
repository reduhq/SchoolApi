from fastapi import FastAPI

from .api.api_v1.api import api_router
from .db.db_setup import engine
from .db.models import user

# user.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="School API",
    description="",
    version="0.0.1",
    contact={
        "Name": "Rey Halsall",
        "Email": "reyeduardohalsallquintero8@gmail.com",
    },
)

app.include_router(api_router)