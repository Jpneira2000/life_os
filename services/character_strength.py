from models.character_strength import CharacterStrengthModel
from schemas.character_strength import CharacterStrengthSchema

class CharacterStrengthService():

    def __init__(self, db) -> None:
        self.db = db

    def create_character_strength(self, character_strength: CharacterStrengthSchema):
        new_character_strength = CharacterStrengthModel(**character_strength.model_dump())
        self.db.add(new_character_strength)
        self.db.commit()
        return