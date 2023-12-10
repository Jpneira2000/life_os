from fastapi import FastAPI
from config.database import engine, Base
from fastapi.responses import HTMLResponse
from routers.pillar import pillar_router
from routers.character_strength import character_strength_router

app = FastAPI()
app.title = 'LifeOS'

app.include_router(pillar_router)
app.include_router(character_strength_router)

Base.metadata.create_all(bind = engine)

@app.get('/', tags = ['home'])
def welcome_message():
    return HTMLResponse('<h1>Welcome to LifeOS</h1>')