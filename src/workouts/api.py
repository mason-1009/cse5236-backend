from ninja import Router
from typing import List
import statistics
import logging
import uuid

from django.shortcuts import get_object_or_404
from django.utils import timezone

from workouts.models import Workout
from workouts.schemas import (
    BaseWorkoutSchema,
    WorkoutOutSchema,
)


router = Router()
logger = logging.getLogger(__file__)


@router.get('/', response=List[WorkoutOutSchema])
def get_user_workouts(request):
    '''
    Returns a time-sorted descending list of workouts.
    '''
    return request.auth.workouts.order_by('-updated')

@router.get('/calc')
def get_daily_workouts(request):
    '''
    Returns aggregate information about a user's daily workout performance.
    '''
    user = request.auth
    response = {
        'calories_burned': 0,
        'duration_minutes': 0,
        'distance_miles': 0
    }

    # Query workouts logged today
    today = timezone.now().replace(hour=0, minute=0, second=0)
    workouts_today = Workout.objects.filter(created__gte=today)

    avg_heart_rate = statistics.mean(
        workouts_today.values_list('avg_heart_rate', flat=True)
    )
    
    max_heart_rate = max(
        workouts_today.values_list('max_heart_rate', flat=True)
    )

    for workout in workouts_today:
        response['duration_minutes'] += workout.duration_minutes
        response['distance_miles'] += workout.distance_miles
        response['calories_burned'] += workout.calories_burned

    response['avg_heart_rate'] = avg_heart_rate
    response['max_heart_rate'] = max_heart_rate

    return response

@router.post('/', response=WorkoutOutSchema)
def record_user_workout(request, body: BaseWorkoutSchema):
    '''
    Records a new workout for a user.
    '''
    user = request.auth
    workout = Workout.objects.create(
        user=user,
        workout_type=body.workout_type,
        duration_minutes=body.duration_minutes,
        distance_miles=body.distance_miles,
        calories_burned=body.calories_burned,
        avg_heart_rate=body.avg_heart_rate,
        max_heart_rate=body.max_heart_rate,
    )
    return workout

@router.delete('/{workout_uuid}')
def delete_user_workout(request, workout_uuid: uuid.UUID):
    '''
    Deletes a workout for a user.
    '''
    user = request.auth
    workout = get_object_or_404(Workout, uuid=workout_uuid)
    
    try:
        workout.delete()
    except Exception as e:
        return { 'success': False, 'detail': str(e) }

    return { 'success': True, 'detail': 'Workout deleted' }
