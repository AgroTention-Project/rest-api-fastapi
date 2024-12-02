"""Module for Plants Models"""

from pydantic import BaseModel, Field


class Classification(BaseModel):
    """Plant Classification Model"""

    kingdom: str
    division: str
    plant_class: str = Field(serialization_alias="class")
    order: str
    family: str
    genus: str
    species: str


class PlantName(BaseModel):
    """Plant Name Model"""

    scientific: str
    local: str
    national: str


class Plant(BaseModel):
    """
    Plant Model
    """

    description: str
    name: PlantName
    classification: Classification
