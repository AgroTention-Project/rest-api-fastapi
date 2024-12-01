from fastapi import FastAPI
from . import (
    app_news,
    app_plants,
    app_root,
    app_users,
)


app = FastAPI()

app.include_router(app_news.router)
app.include_router(app_plants.router)
app.include_router(app_root.router)
app.include_router(app_users.router)
