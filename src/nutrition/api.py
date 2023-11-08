from ninja import Router
from django.shortcuts import get_object_or_404
from typing import List

from nutrition.models import (
    Food,
    NutrientType,
    FoodNutrient,
)
from nutrition.schemas import (
    FoodSchema,
    NutrientTypeSchema,
    FoodNutrientSchema,
    FoodInformationSchema,
    FoodSearchResult,
)
from backend.errors import NotSuperUserError

router = Router()


# Open endpoints
@router.get(
    '/search/{keyword}',
    response=List[FoodSearchResult],
    auth=None
)
def search_food(request, keyword: str):
    '''
    Searches for a keyword and returns the serialized results.
    '''
    RESULT_LIMIT = 30
    results = Food.objects.filter(description__icontains=keyword)

    # Limit results to 30
    return results[0:RESULT_LIMIT]

@router.get(
    '/{fdc_id}',
    response=FoodInformationSchema,
    auth=None
)
def get_food_information(request, fdc_id: int):
    '''
    Get readable food information from fdc_id.
    '''
    food = get_object_or_404(
        Food,
        fdc_id=fdc_id
    )
    return food

@router.post('/admin/food', response=FoodSchema)
def create_food(request, body: FoodSchema):
    '''
    Endpoint to create a food record.
    '''
    if not request.auth.is_superuser:
        raise NotSuperUserError()

    food = Food.objects.create(
        fdc_id=body.fdc_id,
        data_type=body.data_type,
        description=body.description
    )
    return food

@router.post('/admin/nutrient-type', response=NutrientTypeSchema)
def create_nutrient_type(request, body: NutrientTypeSchema):
    '''
    Endpoint to create a nutrient type.
    '''
    if not request.auth.is_superuser:
        raise NotSuperUserError()

    nutrient_type = NutrientType.objects.create(
        nutrient_id=body.nutrient_id,
        name=body.name,
        unit_name=body.unit_name
    )
    return nutrient_type

@router.post('/admin/nutrient')
def create_nutrient(request, body: FoodNutrientSchema):
    '''
    Endpoint to create nutrient information.
    '''
    if not request.auth.is_superuser:
        raise NotSuperUserError()

    food = get_object_or_404(
        Food,
        fdc_id=body.fdc_id
    )
    nutrient_type = get_object_or_404(
        NutrientType,
        nutrient_id=body.nutrient_id
    )
    food_nutrient = FoodNutrient.objects.create(
        food=food,
        nutrient_type=nutrient_type,
        amount=body.amount
    )
    return food_nutrient
