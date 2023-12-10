from models.pillar import PillarModel
from schemas.pillar import PillarSchema

class PillarService():

    def __init__(self, db) -> None:
        self.db = db

    def create_pillar(self, pillar: PillarSchema):
        new_pillar = PillarModel(**pillar.model_dump())
        self.db.add(new_pillar)
        self.db.commit()
        return