from pydantic import BaseModel, Field


class Classification(BaseModel):
    kingdom: str
    division: str
    plant_class: str = Field(serialization_alias="class")
    order: str
    family: str
    genus: str
    species: str


class PlantName(BaseModel):
    scientific: str
    local: str
    national: str


class Plant(BaseModel):
    description: str
    name: PlantName
    classification: Classification
