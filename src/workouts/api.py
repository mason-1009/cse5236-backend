from ninja import Router
from typing import List
import logging

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

@router.post('/', response=WorkoutOutSchema)
def record_user_workout(request, body: BaseWorkoutSchema):
    '''
    Records a new workout for a user.
    '''
    user = request.auth
    workout = Workout.objects.create(
        user=user,
        workout_type=body.workout_type,
        duration=body.duration,
        distance_miles=body.distance_miles,
        calories_burned=body.calories_burned,
        avg_heart_rate=body.avg_heart_rate,
        max_heart_rate=body.max_heart_rate,
        start_datetime=body.start_datetime
    )
    return workout