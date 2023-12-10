from models.character_strength import CharacterStrengthModel
from services.character_strength import CharacterStrengthService

class CharacterStrengthService():

    def __init__(self, db) -> None:
        self.db = db

    def create_character_strength(self, character_strength: CharacterStrengthService):
        new_character_strength = CharacterStrengthModel(**character_strength.model_dump())
        self.db.add(new_character_strength)
        self.db.commit()
        return