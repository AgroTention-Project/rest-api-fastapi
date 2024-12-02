"""
Models for Diseases
"""

from pydantic import BaseModel, Field


class Classification(BaseModel):
    """
    Disease Classification Model
    """

    kingdom: str
    phylum: str
    disease_class: str = Field(serialization_alias="class")
    order: str
    family: str
    genus: str
    species: str


class DiseaseName(BaseModel):
    """
    Disease Name Model
    """

    scientific: str
    local: str
    national: str


class Disease(BaseModel):
    """
    Disease Model
    """

    description: str
    name: DiseaseName
    classification: Classification
