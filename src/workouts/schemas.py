from ninja import Schema
from datetime import datetime, timedelta
from uuid import UUID


class BaseWorkoutSchema(Schema):
    # Model data
    workout_type: str
    duration: timedelta = None

    distance_miles: int = None
    calories_burned: int
    avg_heart_rate: int = None
    max_heart_rate: int = None

    start_datetime: datetime


class WorkoutOutSchema(BaseWorkoutSchema):
    # Mixin data
    created: datetime
    updated: datetime
    uuid: UUID
