from fastapi import APIRouter
from fastapi.responses import JSONResponse
from config.database import Session
from services.pillar import PillarService
from schemas.pillar import PillarSchema

pillar_router = APIRouter()

@pillar_router.post('/pillars', tags=['pillars'], response_model=dict, status_code=201)
def create_pillar(pillar: PillarSchema) -> dict:
    db = Session()
    PillarService(db).create_pillar(pillar)

    return JSONResponse(status_code=201, content={'message': 'Pillar created successfully'})