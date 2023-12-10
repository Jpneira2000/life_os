from fastapi import APIRouter
from fastapi.responses import JSONResponse
from config.database import Session
from services.character_strength import CharacterStrengthService
from schemas.character_strength import CharacterStrengthSchema

character_strength_router= APIRouter()

@character_strength_router.post('/character_strengths', tags=['chatacter_strengths'], response_model=dict, status_code=201)
def create_character_strength(character_strength: CharacterStrengthSchema) -> dict:
    db = Session()
    CharacterStrengthService(db).create_character_strength(character_strength)

    return JSONResponse(status_code=201, content={'message': 'Character Strength created successfully'})