from pydantic import BaseModel, Field


class Classification(BaseModel):
    kingdom: str
    phylum: str
    disease_class: str = Field(serialization_alias="class")
    order: str
    family: str
    genus: str
    species: str


class DiseaseName(BaseModel):
    scientific: str
    local: str
    national: str


class Disease(BaseModel):
    description: str
    name: DiseaseName
    classification: Classification
