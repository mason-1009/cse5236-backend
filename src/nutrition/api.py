from ninja import Router
from django.shortcuts import get_object_or_404
from django.utils import timezone
from typing import List
from uuid import UUID

from nutrition.models import (
    Food,
    NutrientType,
    FoodNutrient,
    Meal,
)
from nutrition.schemas import (
    FoodSchema,
    NutrientTypeSchema,
    FoodNutrientSchema,
    FoodInformationSchema,
    FoodSearchResult,
    BaseMealSchema,
    MealOutSchema,
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
    '/foods{fdc_id}',
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

@router.get('/meals', response=List[MealOutSchema])
def get_meals(request):
    '''
    Returns a list of meals recorded by a user.
    '''
    user = request.auth
    return user.meals.all().order_by('-created')

@router.get('/meals/calc')
def get_daily_macros(request):
    '''
    Returns the sum of macro information today for a user.
    '''
    user = request.auth
    response = {
        'calories': 0,
        'protein_grams': 0,
        'carbs_grams': 0,
        'fat_grams': 0
    }

    # Query meals logged today
    today = timezone.now().replace(hour=0, minute=0, second=0)
    meals_today = Meal.objects.filter(created__gte=today)

    # Accumulate statistics from meals
    for meal in meals_today:
        response['calories'] += meal.calories
        response['protein_grams'] += meal.protein_grams
        response['carbs_grams'] += meal.carbs_grams
        response['fat_grams'] += meal.fat_grams

    return response

@router.post('/meals')
def record_meal(request, body: BaseMealSchema):
    '''
    Records a meal for a user.
    '''
    user = request.auth

    try:
        meal = Meal.objects.create(
            user=user,
            calories=body.calories,
            protein_grams=body.protein_grams,
            carbs_grams=body.carbs_grams,
            fat_grams=body.fat_grams
        )
    except Exception as e:
        return { 'success': False, 'detail': str(e) }

    return { 'success': True, 'detail': 'Recorded meal' }

@router.delete('/meals/{meal_uuid}')
def delete_meal(request, meal_uuid: UUID):
    '''
    Deletes a recorded meal.
    '''
    meal = get_object_or_404(Meal, uuid=meal_uuid)

    try:
        meal.delete()
    except Exception as e:
        return { 'success': False, 'detail': str(e) }

    return { 'success': True, 'detail': 'Deleted meal' }
