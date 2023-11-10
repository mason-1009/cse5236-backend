from ninja import Schema, Field
from typing import List
from uuid import UUID
from datetime import datetime


class FoodSchema(Schema):
    fdc_id: int
    data_type: str
    description: str


class NutrientTypeSchema(Schema):
    nutrient_id: int
    name: str
    unit_name: str


class FoodNutrientSchema(Schema):
    fdc_id: int
    nutrient_id: int
    amount: float


class NutrientOutSchema(Schema):
    nutrient: str = Field(None, alias='nutrient_type.name')
    unit_name: str = Field(None, alias='nutrient_type.unit_name')
    amount: float

class FoodInformationSchema(Schema):
    fdc_id: int
    data_type: str
    description: str

    # Flattened and nested nutrition info
    nutrients: List[NutrientOutSchema]


class FoodSearchResult(Schema):
    fdc_id: int
    data_type: str
    description: str


class BaseMealSchema(Schema):
    calories: int
    protein_grams: int
    carbs_grams: int
    fat_grams: int


class MealOutSchema(BaseMealSchema):
    uuid: UUID
    created: datetime
